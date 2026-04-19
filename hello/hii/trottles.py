from rest_framework.throttling import SimpleRateThrottle

class Throttle(SimpleRateThrottle):
    scope = 'post_limit'

    def get_cache_key(self, request, view):
        if request.method == 'POST' and request.user.is_authenticated:
            return f"throttle_post_{request.user.pk}"
        return None