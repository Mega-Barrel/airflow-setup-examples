
""" Method to Print Astronaut name and craft """

from typing import List

def print_astronauts(**context):
    """
    This task retrieves the list of astronauts from XCom (pushed by a previous task),
    and prints the name of the Astronaut in space and the craft they are flying on.
    """
    ti = context["ti"]
    list_of_people_in_space: List[dict] = ti.xcom_pull(
        task_ids='get_astronauts',
        key='return_value'
    )

    number_of_people = ti.xcom_pull(
        task_ids='get_astronauts',
        key='number_of_people_in_space'
    )

    if not list_of_people_in_space:
        print("XCom data not found or list is empty.")
        return

    print(f"--- There are currently {number_of_people} people in space. ---")
    for astronaut in list_of_people_in_space:
        name = astronaut.get("name", "Unknown Name")
        craft = astronaut.get("craft", "Unknown Craft")
        print(f"Astronaut: **{name}** is on craft: **{craft}**")
