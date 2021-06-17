---
layout: page
title: Spare Ribs
permalink: /bbq/spare_ribs/
parent: BBQ
---
{% assign recipe = site.data.bbq.spareribs_321 %}

# {{ recipe.Name }}
:exclamation:Zuerst herstellen: [BBQ Sauce Süss](/bbq/bbq_sauce_suess/):exclamation:
## Zutaten
{% for ingredient in recipe.Ingredients.Rub -%}
- {{ ingredient }}
{% endfor %}

## Rezept
{% for worksteps in recipe.Worksteps.Rub -%}
1. {{ worksteps }}
{% endfor %}