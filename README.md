# itisnotarecipe

**Overview**

A storage place for all my recipes, with the added spice that they are written in [YAML](https://yaml.org/). These YAML files can be auto-generated into a basic static website.

**Ingredients**

![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=black&color=pink)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black&color=pink)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=black&color=pink)

**Seasoning**

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![try/except style: tryceratops](https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black)](https://github.com/guilatrova/tryceratops)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

<!-- **Sering Suggestions** -->

<!-- ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) -->

**Instructions**
```
Usage: ./create {site|recipe|validate} [null|recipe_name|(y|n)]
```

1. Add new recipe `./create recipe name_of_your_recipe`
2. Add recipe content by updating the generated file at `./recipes/name_of_your_recipe.yaml`
3. Run code clealiness `./create validate`
   - Pass in `n` for a dry run of changes
4. Generate site `./create site`