---
layout: page
title: Pisco Sour
permalink: /cocktails/picso_sour/
parent: Cocktails
---
{% assign recipe = site.data.cocktails.pisco_sour %}
# {{ recipe.Name }}
## Zutaten
{% for ingredient in recipe.Ingredients -%}
- {{ ingredient }}
{% endfor %}

## Rezept
{% for worksteps in recipe.Worksteps -%}
1. {{ worksteps }}
{% endfor %}