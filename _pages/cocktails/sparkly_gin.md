---
layout: page
title: Gin Cava
permalink: /cocktails/sparkly_gin/
parent: Cocktails
---
{% assign recipe = site.data.cocktails.sparkly_gin %}
# {{ recipe.Name }}
## Zutaten
{% for ingredient in recipe.Ingredients -%}
- {{ ingredient }}
{% endfor %}

## Rezept
{% for worksteps in recipe.Worksteps -%}
1. {{ worksteps }}
{% endfor %}


#### Tags
{% for tag in recipe.Tags %}[{{ tag }}](/tags/{{ tag }}) {% endfor %}