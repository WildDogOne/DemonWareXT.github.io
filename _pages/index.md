---
title: Home
layout: page
permalink: /
nav_exclude: true
---
## Cocktails
{% for x in site.data.cocktails -%}
{% for recipe in x -%}
- [{{ recipe.Name }}]({{ recipe.Link }})
{% endfor -%}
{% endfor -%}

## Food
{% for x in site.data.recipes -%}
{% for recipe in x -%}
- [{{ recipe.Name }}]({{ recipe.Link }})
{% endfor -%}
{% endfor -%}
