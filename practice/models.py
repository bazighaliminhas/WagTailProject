from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.blocks import (
    CharBlock, TextBlock, DateBlock, 
    StructBlock, StreamBlock
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from modelcluster.fields import ParentalKey


# ============================================
# STREAMFIELD BLOCKS FOR CARDS SECTION
# ============================================

class CardBlock(StructBlock):
    """Individual card block for featured articles"""
    image = ImageChooserBlock(required=False, help_text="Card image")
    title = CharBlock(max_length=100, help_text="Card title")
    description = TextBlock(help_text="Card description")
    publish_date = DateBlock(help_text="Publication date")
    
    class Meta:
        icon = 'doc-full'
        label = 'Article Card'
        template = 'practice/blocks/card_block.html'


# ============================================
# MAIN PRACTICE PAGE MODEL
# ============================================

class PracticePage(Page):
    """
    Main practice page model with translation support
    """
    
    # HERO SECTION FIELDS
    hero_title = models.CharField(
        max_length=200,
        default="Wagtail CMS Test Page",
        help_text="Main hero title"
    )
    hero_subtitle = models.TextField(
        default="This page is created to test Wagtail Page Models, Fields, and StreamField concepts.",
        help_text="Hero subtitle/description"
    )
    hero_publish_date = models.DateField(
        help_text="Display publish date in hero section"
    )
    
    # ABOUT SECTION
    about_title = models.CharField(
        max_length=200,
        default="About This Page",
        help_text="About section title"
    )
    about_content = RichTextField(
        help_text="Rich text content for about section"
    )
    
    # SIDEBAR INFO
    author = models.CharField(
        max_length=100,
        default="Admin User",
        help_text="Page author name"
    )
    category = models.CharField(
        max_length=100,
        default="CMS Practice",
        help_text="Page category"
    )
    status = models.CharField(
        max_length=50,
        default="Published",
        help_text="Page status"
    )
    last_updated = models.DateField(
        auto_now=True,
        help_text="Last update date"
    )
    
    # CARDS SECTION - SEPARATE STREAMFIELDS FOR EACH LANGUAGE
    featured_articles = StreamField(
        [
            ('card', CardBlock()),
        ],
        blank=True,
        use_json_field=True,
        help_text="Add featured article cards (English)",
        verbose_name="Featured Articles (English)"
    )
    
    # featured_articles_ar = StreamField(
    #     [
    #         ('card', CardBlock()),
    #     ],
    #     blank=True,
    #     use_json_field=True,
    #     help_text="Add featured article cards (Arabic)",
    #     verbose_name="Featured Articles (Arabic)"
    # )
    
    # FORM SECTION TITLE
    form_section_title = models.CharField(
        max_length=200,
        default="Contact / Form Testing",
        help_text="Form section title"
    )
    
    # CONTENT PANELS (Admin Interface)
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_title'),
                FieldPanel('hero_subtitle'),
                FieldPanel('hero_publish_date'),
            ],
            heading="Hero Section",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('about_title'),
                FieldPanel('about_content'),
            ],
            heading="About Section",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('author'),
                FieldPanel('category'),
                FieldPanel('status'),
            ],
            heading="Sidebar Information",
            classname="collapsible"
        ),
        FieldPanel('featured_articles'),
        # MultiFieldPanel(
        #     [
        #         FieldPanel('featured_articles),
        #         FieldPanel('featured_articles_ar'),
        #     ],
        #     heading="Featured Articles (Both Languages)",
        #     classname="collapsible"
        # ),
        FieldPanel('form_section_title'),
    ]
    
    class Meta:
        verbose_name = "Practice Page"


# ============================================
# FORM PAGE MODEL (For Contact Form)
# ============================================

class FormField(AbstractFormField):
    """Custom form field for the contact form"""
    page = ParentalKey(
        'ContactFormPage',
        on_delete=models.CASCADE,
        related_name='form_fields'
    )


class ContactFormPage(AbstractEmailForm):
    """
    Contact form page with custom fields
    """
    intro = RichTextField(blank=True, help_text="Form introduction text")
    thank_you_text = RichTextField(
        blank=True,
        help_text="Text to display after form submission"
    )
    
    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        FieldPanel('thank_you_text'),
    ]
    
    class Meta:
        verbose_name = "Contact Form Page"
