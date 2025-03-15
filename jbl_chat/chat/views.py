from django.shortcuts import render


def hello_world(request):
    return render(request, 'chat/mock_page.html')


def mock_page(request):
    return render(request, 'chat/mock_page.html')


def mock_messages(request):
    return render(request, 'chat/mock_messages.html')
