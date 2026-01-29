from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import PracticePage, ContactFormPage


@register(PracticePage)
class PracticePageTR(TranslationOptions):
    """
    Translation options for PracticePage
    """
    fields = (
        'hero_title',
        'hero_subtitle',
        'about_title',
        'about_content',
        'author',
        'category',
        'status',
        'form_section_title',
    )


@register(ContactFormPage)
class ContactFormPageTR(TranslationOptions):
    """
    Translation options for ContactFormPage
    """
    fields = (
        'intro',
        'thank_you_text',
    )
