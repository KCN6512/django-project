from jinja2 import Template

cities = [
    {'id': 1,'city': 'Кропоткин'},
    {'id': 2,'city': 'Краснодар'},
    {'id': 3,'city': 'Армавир'},
    {'id': 4,'city': 'Гулькевичи'},
    {'id': 5,'city': 'Пенза'},
    {'id': 6,'city': 'Тамриэль'}
] 

data = """<select name='cities'>
{% for i in cities -%}
{% if i.id > 5 -%}
    <option value='{{ i['id'] }}'>{{ i['city'] }}</option>
{% else -%}
    {{ i['id'] }}
{% endif -%}
{% endfor -%}
</select>"""

tm = Template(data)
msg = tm.render(cities=cities)

print(msg)


