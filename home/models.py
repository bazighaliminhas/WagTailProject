# home/models.py - check what fields exist
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    # Check what fields are here
    # Common fields might be: body, intro, etc.
    pass
