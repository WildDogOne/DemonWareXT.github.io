---
title: Home
layout: page
permalink: /
nav_exclude: true
---
Willkommen bei meiner kochen und anderes Seite

## Cocktails
{% for x in site.data.cocktails -%}
{% for recipe in x -%}
{% for y in recipe.Tags -%}
- [{{ recipe.Name }}]({{ recipe.Link }})
{% endfor -%}
{% endfor -%}
{% endfor -%}
