from jinja2 import Template

# 1
#
# items = [
#     {'item': 'index', 'content': 'Главная'},
#     {'item': 'news', 'content': 'Новости'},
#     {'item': 'about', 'content': 'О компании'},
#     {'item': 'shop', 'content': 'Магазин'},
#     {'item': 'contacts', 'content': 'Контакты'}
# ]
# link = """
# <ul>
# {% for i in items -%}
# {%- if i.content=='Главная' -%}
# <li><a href='/{{i.item}}' class='active'>{{i.content}}</a></li>
# {%- else %}
# <li><a href='/{{i['item']}}'>{{i['content']}}</a></li>
# {%- endif -%}
# {%- endfor %}
# </ul>
# """
# tm = Template(link)
# msg = tm.render(items=items)
#
# print(msg)

# 2

html = """
{%-macro text_input(name, placeholder, type='text') -%}
    <input type='{{type}}' name='{{name}}' placeholder='{{placeholder}}'>
{%- endmacro -%}  
<p>{{text_input('firstname', 'Имя')}}</p>
<p>{{text_input('lastname', 'Фамилия')}}</p>
<p>{{text_input('address', 'Адрес')}}</p>
<p>{{text_input('phone', 'Телефон', type='tel')}}</p>
<p>{{text_input('email', 'Почта', type='email')}}</p>
  
"""

tm = Template(html)
msg = tm.render()

print(msg)
