from django.shortcuts import render
from django.http import Http404

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]

post_positions = {post['id']: i for i, post in enumerate(posts)}


def index(request):
    sorted_posts = sorted(posts, key=lambda post: post['id'], reverse=True)
    return render(request, 'blog/index.html', {'posts': sorted_posts})


def post_detail(request, id):
    if id not in post_positions:
        raise Http404('Неправильно набран адрес, '
                      'или такой страницы на сайте больше не существует.')
    return render(request, 'blog/detail.html',
                  {'post': posts[post_positions[id]]})


def category_posts(request, category_slug):
    context = {'category': category_slug}
    return render(request, 'blog/category.html', context)


'''
# Если нужно вывести название категории и все посты в ней
def category_posts(request, category_slug):
    sorted_posts = [post for post in posts if
                    post['category'] == category_slug]
    context = {'category': category_slug,
               'posts': sorted_posts}
    return render(request, 'blog/category.html', context)
# также в templates/blog/category.html добавить
  {% if posts %}
    {% include "includes/posts_list.html" %}
  {% endif %}
'''
