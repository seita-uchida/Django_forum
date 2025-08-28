from django.shortcuts import render

from .models import Topic, Message


def index(request):
    TOPIC_LIST = Topic.objects.all()
    context = {
        "topics": TOPIC_LIST,
    }
    return render(request, "main/index.html", context)


def forum(request, topic_name):
    topic = Topic.objects.get(name=topic_name)
    messages = Message.objects.filter(topic=topic).order_by("created_at")
    context = {
        "messages": messages,
        "topic": topic,
    }
    return render(request, "main/forum.html", context)