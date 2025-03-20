from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from chat.forms import ChatForm
from chat.models import Profile, Message


def hello_world(request):
    return render(request, "chat/mocks/mock_page.html")


def mock_page(request):
    return render(request, "chat/mocks/mock_page.html")


def mock_messages(request):
    return render(request, "chat/mocks/mock_messages.html")


def mock_login(request):
    form = AuthenticationForm()
    return render(request, "chat/mocks/mock_login.html", {"form": form})


def index(request):
    return render(request, "chat/index.html")


def about(request):
    return render(request, "chat/about.html")


def api_index(request):
    return render(request, "chat/api.html")


@method_decorator(login_required, name="dispatch")
class ChatFormView(FormView):
    template_name = "chat/chat.html"
    form_class = ChatForm

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user__username=self.kwargs["nickname"])
        instance = form.save(commit=False)
        instance.sender = self.request.user.profile
        instance.receiver = profile
        instance.save()
        # If the request is an htmx request, return a partial response (just the messages)
        if self.request.htmx:
            return self.get_partial_response()
        else:  # Otherwise, return the full page, by redirecting to the same page
            return super().form_valid(form)

    def get_success_url(self):
        # Stay on the same page after sending the message
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_profile = self.request.user.profile
        other_profile = get_object_or_404(Profile, user__username=self.kwargs["nickname"])
        messages = Message.objects.conversation_between(this_profile, other_profile)
        context["chat_profiles"] = Profile.objects.exclude(user=self.request.user)
        context["profile"] = other_profile
        context["messages"] = messages
        return context

    def get_partial_response(self):
        return render(
            self.request, "chat/partials/messages.html", self.get_context_data()
        )

    def get_template_names(self):
        if self.request.htmx:
            return ["chat/partials/messages.html"]
        return super().get_template_names()
