from pprint import pprint

import yaml


def yaml_read(inputyaml):
    with open(inputyaml, mode="r", encoding="utf-8") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def generate_cocktail_page(cocktail_id, cocktail):
    file = "_pages/cocktails/" + cocktail_id + ".md"
    f = open(file, "w")
    f.write("---\n")
    f.write("layout: page\n")
    f.write("title: " + cocktail["Name"] + "\n")
    f.write("permalink: " + cocktail["Link"] + "\n")
    f.write("parent: Cocktails\n")
    f.write("---\n")
    f.write("{% assign recipe = site.data.cocktails." + cocktail_id + " %}\n")
    f.write("{% include cocktail.liquid %}")
    f.close()


def generate_recipe_page(recipe_id, recipe):
    pprint(recipe)
    file = "_pages" + recipe["Link"] + ".md"
    pprint(file)
    quit()
    f = open(file, "w")
    f.write("---\n")
    f.write("layout: page\n")
    f.write("title: " + cocktail["Name"] + "\n")
    f.write("permalink: " + cocktail["Link"] + "\n")
    f.write("parent: Cocktails\n")
    f.write("---\n")
    f.write("{% assign recipe = site.data.cocktails." + recipe_id + " %}\n")
    f.write("{% include cocktail.liquid %}")
    f.close()


def generate_cocktail_tags(tags):
    for tag in tags:
        file = "_pages/cocktails/tags/" + tag.lower().replace(" ", "_") + ".md"
        f = open(file, "w")
        f.write("---\n")
        f.write("layout: page\n")
        f.write("title: " + tag + "\n")
        f.write("permalink: /cocktails/tags/" + tag + "/\n")
        f.write("parent: Tags\n")
        f.write("grand_parent: Cocktails\n")
        f.write("---\n")
        f.write("{% assign tag = \"" + tag + "\" %}\n")
        f.write("# {{ tag }}\n")
        f.write("{% include cocktail_tags.liquid %}")
        f.close()


def generate_cocktails(inputyaml):
    cocktails = yaml_read(inputyaml)
    tags = []
    for cocktail in cocktails:
        generate_cocktail_page(cocktail, cocktails[cocktail])
        for tag in cocktails[cocktail]["Tags"]:
            if tag not in tags:
                tags.append(tag)
    generate_cocktail_tags(tags)


def generate_food(inputyaml):
    recipes = yaml_read(inputyaml)
    for recipe in recipes:
        generate_recipe_page(recipe, recipes[recipe])


def main():
    print("Generating Cocktail Pages")
    generate_cocktails("_data/cocktails.yml")
    print("Generating Food Pages")
    generate_food("_data/recipes.yml")
    print("Done")


if __name__ == "__main__":
    main()
