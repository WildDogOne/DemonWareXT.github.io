---
layout: single
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