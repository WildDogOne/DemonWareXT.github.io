---
layout: page
title: BBQ Sauce Süss
permalink: /bbq/bbq_sauce_suess/
parent: BBQ
---
{% assign recipe = site.data.bbq.bbq_sauce %}

# {{ recipe.Name }}
## Zutaten
{% for ingredient in recipe.Ingredients.Sauce -%}
- {{ ingredient }}
{% endfor %}

## Rezept
{% for worksteps in recipe.Worksteps.Sauce -%}
1. {{ worksteps }}
{% endfor %}

