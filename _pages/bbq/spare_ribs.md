---
layout: page
title: Spare Ribs
permalink: /bbq/spare_ribs/
parent: BBQ
---
{% assign recipe = site.data.bbq.spareribs_321 %}

# {{ recipe.Name }}
## Zutaten
{% for ingredientStep in recipe.Ingredients %}
- {{ ingredientStep }}
{% for ingredient in ingredientStep %}
- {{ ingredient }}
{% endfor %}
{% endfor %}

   
{% for wheel in site.data.ywheels %}
{% if wheel.Brand == "Rexing" %}

## {% if wheel.Brand %}{{ wheel.Brand }} - {% endif %}{% if wheel.Model %}{{ wheel.Model }}<br>{% endif %}
{% if wheel.Brand %}Brand: {{ wheel.Brand }}<br>{% endif %}
{% if wheel.Model %}Model: {{ wheel.Model }}<br>{% endif %}
{% if wheel.Style %}Wheel Style: {{ wheel.Style }}<br>{% endif %}
{% if wheel.Screen %}Screen: {{ wheel.Screen }}<br>{% endif %}
{% if wheel.Width_MM %}Width: {{ wheel.Width_MM }} mm<br>{% endif %}
{% if wheel.LINK %}Link to Product: {{ wheel.LINK }}<br>{% endif %}
{% if wheel.RETAIL_EU %}Price EU: {{ wheel.RETAIL_EU }} EUR<br>{% endif %}
{% if wheel.RETAIL_US %}Price US: {{ wheel.RETAIL_US }} USD<br>{% endif %}
{% if wheel.Comment %}Comments: {{ wheel.Comment }} USD<br>{% endif %}

---
{% endif %}
{% endfor %}