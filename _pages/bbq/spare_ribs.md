---
layout: page
title: Spare Ribs
permalink: /bbq/spare_ribs/
parent: BBQ
---
{% assign recipe = site.data.bbq.spareribs_321 %}

# {{ recipe.Name }}
## Zutaten
{% for ingredient in recipe.Ingredients.Rub %}
- {{ ingredient }}
{% endfor %}

## Rezept
{% for worksteps in recipe.Worksteps.Rub %}
- {{ worksteps }}
{% endfor %}


{% assign recipe = site.data.bbq.bbq_sauce %}

# {{ recipe.Name }}
## Zutaten
{% for ingredient in recipe.Ingredients.Sauce %}
- {{ ingredient }}
{% endfor %}

## Rezept
{% for worksteps in recipe.Worksteps.Sauce %}
- {{ worksteps }}
{% endfor %}

