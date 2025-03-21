from django.utils import timezone


def last_seen_middleware(get_response):
    """
    Middleware that updates the last seen timestamp for the current user.
    """

    def middleware(request):
        response = get_response(request)
        if request.user.is_authenticated:
            request.user.profile.last_seen = timezone.now()
            request.user.profile.save()
        return response

    return middleware
