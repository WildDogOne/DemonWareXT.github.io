# Opensource Cooking

[https://demonwarext.github.io/](https://demonwarext.github.io/)

This is my simple cookbook based on Jekyll.
It was built out of frustration of the internet when it comes to cooking ressources, because let's be honest, we don't all have time to read through these huge food blogs with so little actually relevant information.

## Ways to contribute

- Add recipes or cocktail ideas
- Fix errors in recipes or add improvements

## Rules for submission

- All recipes are to be added into the yaml files (_data/*.yml) and follow the standard schema
- Language of this repository is German, fork it if you want to translate

### Tags

You can (and should) add tags at the end of your recipe.
However it's only really relevant at the moment for Cocktails

List of special, categorical tags to use if relevant:
- `mixology`: for recipes used to make cocktail ingredients
- `summer`: for hot time recipes
- `winter`: for winter recipes

### Schema
#### Cocktail
```
name_of_cocktail:
  Name: Name of Cocktail
  Link: /cocktails/name_of_cocktail/
  Rating: 4
  Tags:
    - Tag 1
    - Tag 2
  Worksteps:
    - Step 1
    - Step 2
  Ingredients:
    - Ingredient 1
    - Ingredient 2
```


## About the site

Most jekyll files are generated automatically
The most important thing is to get the YAML files sorted correctly
Improvements to the templates are definitelly welcome and needed
