from django.http import HttpResponseBadRequest

# custom ajax_required decorator(function that extend another)
def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            # returns an HttpResponseBadRequest object (HTTP 400
            #if the request is not AJAX
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap