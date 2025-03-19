from chat.models import Profile


def navigation_processor(request):
    if not request.user.is_authenticated:
        return {}
    chat_profiles = Profile.objects.exclude(user=request.user)
    return {"available_chats": chat_profiles}
