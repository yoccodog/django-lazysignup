from lazysignup.decorators import allow_lazy_user

class LazyMiddleware:
    def __init__(self, get_response):
        self.get_response = allow_lazy_user(get_response)
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
