from django.utils import translation

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip language switching for admin pages
        if request.path.startswith('/admin'):
            translation.activate('en')
            request.LANGUAGE_CODE = 'en'
            response = self.get_response(request)
            return response
        
        # Check if language is in query parameter
        lang = request.GET.get('lang')
        
        if lang and lang in ['en', 'ar']:
            translation.activate(lang)
            request.LANGUAGE_CODE = lang
            response = self.get_response(request)
            response.set_cookie('django_language', lang, max_age=31536000)
            return response
        
        # Check cookie
        lang = request.COOKIES.get('django_language')
        if lang and lang in ['en', 'ar']:
            translation.activate(lang)
            request.LANGUAGE_CODE = lang
        else:
            translation.activate('en')
            request.LANGUAGE_CODE = 'en'
        
        response = self.get_response(request)
        return response