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
{% assign recipes_by_name = site.data.recipes | sort %}
{% for x in recipes_by_name -%}
{% for recipe in x -%}
{% if recipe.Name -%}
- [{{ recipe.Name }}]({{ recipe.Link }}) - {{ recipe.Region }}
{% endif %}
{% endfor -%}
{% endfor -%}

## Smoothies
{% assign smoothies_by_name = site.data.smoothies | sort %}
{% for x in smoothies_by_name -%}
{% for recipe in x -%}
- [{{ recipe.Name }}]({{ recipe.Link }})
{% endfor -%}
{% endfor -%}