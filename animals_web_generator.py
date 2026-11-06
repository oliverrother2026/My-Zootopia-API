import os
import requests
from dotenv import load_dotenv


def get_animals_data(animal_name):
    load_dotenv(dotenv_path=".env", override=True)

    api_key = os.getenv("API_KEY")

    url = "https://api.api-ninjas.com/v1/animals"

    response = requests.get(
        url,
        headers={"X-Api-Key": api_key},
        params={"name": animal_name},
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def serialize_animal(animal_obj):
    output = ""
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul class="card__details">\n'

    if "characteristics" in animal_obj:
        if "diet" in animal_obj["characteristics"]:
            output += f'<li class="card__detail"><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n'

    if "locations" in animal_obj:
        if animal_obj["locations"]:
            output += f'<li class="card__detail"><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'

    if "characteristics" in animal_obj:
        if "type" in animal_obj["characteristics"]:
            output += f'<li class="card__detail"><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'

    if "characteristics" in animal_obj:
        if "lifespan" in animal_obj["characteristics"]:
            output += f'<li class="card__detail"><strong>Lifespan:</strong> {animal_obj["characteristics"]["lifespan"]}</li>\n'

    if "characteristics" in animal_obj:
        if "temperament" in animal_obj["characteristics"]:
            output += f'<li class="card__detail"><strong>Temperament:</strong> {animal_obj["characteristics"]["temperament"]}</li>\n'

    if "taxonomy" in animal_obj:
        if "scientific_name" in animal_obj["taxonomy"]:
            output += f'<li class="card__detail"><strong>Scientific Name:</strong> {animal_obj["taxonomy"]["scientific_name"]}</li>\n'

    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"

    return output


animal_name = input("Enter a name of an animal: ")
animals_data = get_animals_data(animal_name)

#print("Anzahl gefundener Tiere:", len(animals_data))
#print("Tiernamen:", [animal["name"] for animal in animals_data])

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

# print(html_template)


output = ""

for animal in animals_data:
    output += serialize_animal(animal)

# print(output)

html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Website was successfully generated to the file animals.html.")
