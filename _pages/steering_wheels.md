---
#layout: single
layout: page
title: Steering Wheels
permalink: /hardware/wheels/
classes:
 - wide
---
{% comment %}
<table>
  {% for row in site.data.wheels %}
    {% if forloop.first %}
    <tr style="color:#eaeaea; background-color:#51555d; border-bottom:2px solid #3d4046;">
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>
{% endcomment %}

# Wheels 

{% for wheel in site.data.ywheels %}
<p>
{% if wheel.Brand %}Brand: {{ wheel.Brand }}<br>{% endif %}
{% if wheel.Model %}Model: {{ wheel.Model }}<br>{% endif %}
{% if wheel.Style %}Wheel Style: {{ wheel.Style }}<br>{% endif %}
{% if wheel.Screen %}Screen: {{ wheel.Screen }}<br>{% endif %}
{% if wheel.Width_MM %}Width: {{ wheel.Width_MM }} mm<br>{% endif %}
{% if wheel.LINK %}Link to Product: {{ wheel.LINK }}<br>{% endif %}
{% if wheel.RETAIL_EU %}Price EU: {{ wheel.RETAIL_EU }} EUR<br>{% endif %}
{% if wheel.RETAIL_US %}Price US: {{ wheel.RETAIL_US }} USD<br>{% endif %}
</p>
---
{% endfor %}

# Wheel overview table
<table>
    <tbody>
    <tr style="color:#eaeaea; background-color:#51555d; border-bottom:2px solid #3d4046;">
            <th>Brand</th>
            <th>Model</th>
            <th>LINK</th>
            <th>Style</th>
            <th>Width MM</th>
            <th>RETAIL EU</th>
            <th>RETAIL US</th>
    </tr>
        {% for wheel in site.data.ywheels %}
          <tr>
            <td>{{ wheel.Brand }}</td>
            <td>{{ wheel.Model }}</td>
            <td>{{ wheel.LINK }}</td>
            <td>{{ wheel.Style }}</td>
            <td>{{ wheel.Width_MM }}</td>
            <td>{{ wheel.RETAIL_EU }}</td>
            <td>{{ wheel.RETAIL_US }}</td>
          </tr>
        {% endfor %}
    </tbody>
</table>