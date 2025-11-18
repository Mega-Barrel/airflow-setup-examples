
""" Method to call Astronaut Real Time API """

from typing import List
import requests

def get_astronauts(**context) -> List[dict]:
    """
    This task uses the request library to retrieve a list of Astronauts
    currently in space. Results are pushed to XCom, to be consumed in a downstream
    pipeline.
    
    Returns:
        (number_of_people_in_space, list_of_people_in_space)
    """
    try:
        response = requests.get("http://api.open-notify.org/astros.json", timeout=300)
        response.raise_for_status()
        data = response.json()

        number_of_people_in_space = data["number"]
        list_of_people_in_space = data["people"]

        # Push number to XCom
        context["ti"].xcom_push(
            key="number_of_people_in_space",
            value=number_of_people_in_space
        )
        return list_of_people_in_space

    except requests.exceptions.ConnectionError as exc:
        raise requests.exceptions.ConnectionError("Failed to connect to the server.") from exc
    except requests.exceptions.Timeout as exc:
        raise requests.exceptions.Timeout("Request timed out.") from exc
    except requests.exceptions.HTTPError as exc:
        raise requests.exceptions.HTTPError("HTTP error occurred.") from exc
    except Exception as exc:
        raise RuntimeError(f"An unexpected non-request-related error occurred: {exc}") from exc
