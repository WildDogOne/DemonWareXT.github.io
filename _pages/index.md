---
title: Home
layout: page
permalink: /
nav_exclude: true
---
## Cocktails
{% assign cocktail_by_name = site.data.cocktails | sort %}
{% for x in cocktail_by_name -%}
{% for recipe in x -%}
- [{{ recipe.Name }}]({{ recipe.Link }})
{% endfor -%}
{% endfor -%}

## Essen
{% for x in site.data.recipes -%}
{% for recipe in x -%}
- [{{ recipe.Name }}]({{ recipe.Link }})
{% endfor -%}
{% endfor -%}

## Smoothies
{% for x in site.data.smoothies -%}
{% for recipe in x -%}
- [{{ recipe.Name }}]({{ recipe.Link }})
{% endfor -%}
{% endfor -%}