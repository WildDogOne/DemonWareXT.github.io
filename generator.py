from pprint import pprint

import yaml


def yaml_read(inputyaml):
    with open(inputyaml, mode="r", encoding="utf-8") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def generate_cocktail_page(cocktail_id, cocktail):
    pprint(cocktail)
    file = "_pages/cocktails/" + cocktail_id + ".md"
    f = open(file, "w")
    f.write("---\n")
    f.write("layout: page\n")
    f.write("title: "+cocktail["Name"]+"\n")
    f.write("permalink: "+cocktail["Link"]+"\n")
    f.write("parent: Cocktails\n")
    f.write("---\n")
    f.write("{% assign recipe = site.data.cocktails."+cocktail_id+" %}\n")
    f.write("{% include cocktail.liquid %}")
    f.close()
    #quit()
"""
---
layout: page
title: Pisco Sour
permalink: /cocktails/pisco_sour/
parent: Cocktails
---
{% assign recipe = site.data.cocktails.pisco_sour %}
{% include cocktail.liquid %}
"""

def generate_cocktails(inputyaml):
    cocktails = yaml_read(inputyaml)
    tags = []
    for cocktail in cocktails:
        generate_cocktail_page(cocktail, cocktails[cocktail])
        for tag in cocktails[cocktail]["Tags"]:
            if tag not in tags:
                tags.append(tag)
    pprint(tags)


def main():
    generate_cocktails("_data/cocktails.yml")


if __name__ == "__main__":
    main()
