---
title: Home
layout: page
permalink: /
nav_exclude: true
---
## Cocktails
{% for x in site.data.cocktails -%}
{% for recipe in x|sort(attribute='Name') -%}
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