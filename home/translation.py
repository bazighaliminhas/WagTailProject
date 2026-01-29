from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import HomePage


@register(HomePage)
class HomePageTR(TranslationOptions):
    """
    Translation options for HomePage
    """
    fields = ()
