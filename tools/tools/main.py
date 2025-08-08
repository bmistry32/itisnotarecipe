from os import listdir, path
from typing import Any
from jinja2 import Environment, FileSystemLoader, Template
import yaml

YAML_INPUT_PATH: str = "./recipes"
HTML_OUTPUT_PATH: str = "./static/site"
RECIPES_BY_TAG: dict = {}
RECIPES_BY_DIET: dict = {}

env = Environment(loader=FileSystemLoader("./tools/templates"))


class RecipeGeneratorError(Exception):
    pass


def _add_to_homepage(recipe: dict, filename: str) -> None:
    tags = recipe.get("tags", [])
    recipes = RECIPES_BY_TAG
    for tag in tags:
        if tag not in recipes:
            RECIPES_BY_TAG[tag] = []
        RECIPES_BY_TAG[tag].append(
            {
                "title": recipe["title"],
                "filename": filename,
            }
        )
    diet = recipe.get("diet", [])
    recipes_d = RECIPES_BY_DIET
    for tag in diet:
        if tag not in recipes_d:
            RECIPES_BY_DIET[tag] = []
        RECIPES_BY_DIET[tag].append(
            {
                "title": recipe["title"],
                "filename": filename,
            }
        )


def _get_template(file: str) -> Template:
    template = f"{file}.html"
    return env.get_template(template)


def _sort_dict(to_sort) -> dict:
    return dict(sorted(to_sort.items()))


def _write_html_file(file_name: str, contents: Any) -> str:
    filepath = path.join(f"./{HTML_OUTPUT_PATH}/", file_name)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(contents)
    return f"Generated {filepath} successfuly"


def generate_recipes() -> None:
    template = _get_template("recipe")

    for filename in listdir(YAML_INPUT_PATH):
        if not filename.endswith(".yaml"):
            continue
        yaml_file = path.join(YAML_INPUT_PATH, filename)
        try:
            with open(yaml_file, "r", encoding="utf-8") as file:
                recipe = yaml.safe_load(file)
        except (FileNotFoundError, yaml.YAMLError) as err:
            raise RecipeGeneratorError(err) from err
        try:
            html = template.render(recipe)
            html_file_name = filename.replace("yaml", "html")
            write_ouput = _write_html_file(html_file_name, html)
            print(write_ouput)
        except IOError as err:
            raise RecipeGeneratorError(err) from err
        _add_to_homepage(recipe, html_file_name)
    print("All HTML files generated successfully!")


def generate_homepage() -> None:
    if not RECIPES_BY_TAG:
        return
    template = _get_template("homepage")
    try:
        homepage_template = template.render(
            recipes_by_tag=_sort_dict(RECIPES_BY_TAG), recipes_by_diet=_sort_dict(RECIPES_BY_DIET)
        )
        write_ouput = _write_html_file("index.html", homepage_template)
        print(write_ouput)
    except IOError as err:
        raise RecipeGeneratorError(err) from err


if __name__ == "__main__":
    try:
        generate_recipes()
        generate_homepage()
    except RecipeGeneratorError as err:
        print(err)
