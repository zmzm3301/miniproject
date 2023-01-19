from django.shortcuts import render
from blog.models import Post


def index(request):
    if request.method == "POST":
        bat = request.POST['battery']
        led_color = request.POST['led_color']

        p = Post()

        print("모델의 타입 : ", type(p))
        print("모델의 형상 : ", p)

        p.battery = bat
        p.led_color = led_color

        p.save()
        return render(
            request,
            'blog/index.html',
            {
                'bat': bat,
                'led_color': led_color,
            }
        )

    if request.method == "GET":
        posts = Post.objects.all()
        return render(
            request,
            'blog/index.html',
            {
                "posts": posts
            }
        )
