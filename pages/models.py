from __future__ import absolute_import, unicode_literals

from django.db import models
from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.response import TemplateResponse

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel

from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from wagtail.core.blocks import TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock, BooleanBlock, ChoiceBlock, PageChooserBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock


from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaEmailForm


class AlignmentChoiceBlock(ChoiceBlock):
    choices = [
        ('normal', 'Normal'),
        ('float-left', 'Left'),
        ('text-center', 'Center'),
        ('float-right', 'Right'),
        ('text-justify', 'Justify'),
        ('text-nowrap', 'No Wrap')
    ]


class AlignedRAWHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = AlignmentChoiceBlock(default='normal')


class BackgroundColorBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), 
        ('concrete', 'Concrete')
    ))


class FontAwesomeIconSizeBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('lg', 'fa-lg'), 
        ('2x', 'fa-2x'),
        ('3x', 'fa-3x'),
        ('4x', 'fa-4x'),
        ('5x', 'fa-5x'),
    ))

class FontAwesomeIconTypeBlock(ChoiceBlock):
    choices = [
        ('regular', 'Regular'),
        ('brand', 'Brand')
    ]


class MaterialIconSizeBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('18', '18'), 
        ('24', '24'),
        ('36', '36'),
        ('48', '48'),
        ('60', '60'),
        ('72', '72'),
        ('84', '84'),
        ('96', '96'),
        ('108', '108'),
        ('120', '120'),
    ))


class PullQuoteBlock(StructBlock):
    quote = TextBlock('quote title')
    attribution = CharBlock()

    class Meta:
        icon = 'openquote'


class IconBlock(StructBlock):
    font_awesome_icon_name = CharBlock(required=False)
    font_awesome_icon_size = FontAwesomeIconSizeBlock()
    font_awesome_icon_choice = FontAwesomeIconTypeBlock(required=False, default='regular')
    material_icon_name = CharBlock(required=False)
    material_icon_size = MaterialIconSizeBlock()
    alignment = AlignmentChoiceBlock(default='normal')

    class Meta:
        label = 'Icon'


class HtmlFormatBlock(StreamBlock):
    h1 = CharBlock(classname='title', help_text='Always use only one H1 per page')
    h2 = CharBlock(classname='title')
    h3 = CharBlock(classname='title')
    h4 = CharBlock(classname='title')
    paragraph = RichTextBlock()
    table = TableBlock(template='includes/table.html')
    image = ImageChooserBlock()
    document = DocumentChooserBlock(icon='doc-full-inverse')
    embedded_video = EmbedBlock()
    lead_body = CharBlock(classname='lead')
    small_text = CharBlock(classname='small')
    blockquote = CharBlock(classname='blockquote')
    pull_quote = PullQuoteBlock()
    icon = IconBlock()
    raw_html = AlignedRAWHTMLBlock()


class StarFishBlock(StructBlock):
    html = RawHTMLBlock()

    class Meta:
        template = 'starfish_block.html'
        label = 'Starfish'


class SingleColumnBlock(StructBlock):
    column = HtmlFormatBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'single_column_block.html'
        label = 'Single Column'


class TwoColumnBlock(StructBlock):
    left_column = HtmlFormatBlock()
    right_column = HtmlFormatBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'two_column_block.html'
        label = 'Two Columns'


class ThreeColumnBlock(StructBlock):
    left_column = HtmlFormatBlock()
    middle_column = HtmlFormatBlock()
    right_column = HtmlFormatBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'three_column_block.html'
        label = 'Three Columns'


class FourColumnBlock(StructBlock):
    left_column_1 = HtmlFormatBlock()
    left_column_2 = HtmlFormatBlock()
    right_column_1 = HtmlFormatBlock()
    right_column_2 = HtmlFormatBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'four_column_block.html'
        label = 'Four Columns'


class HeroImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    alternate_text = CharBlock(help_text='Text for screen readers')
    caption = CharBlock(required=False, max_length=120, help_text='Caption will be shown below the image')
    fine_print = CharBlock(required=False, max_length=120, help_text='Fine Print will be shown below caption')
    overlay_text = BooleanBlock(required=False, help_text='If checked, caption is overlayed on image')
    photo_credit = CharBlock(required=False, max_length=80, help_text='This will show bottom right on the image. Make sure overlay text is checked')
    photo_credit_link = CharBlock(required=False, max_length=200, help_text='If you would like the above text to link to a website. Enter complete URL here.')

    class Meta:
        template = 'hero_image_block.html'


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(WagtailCaptchaEmailForm):
    body = StreamField([
        ('hero_image', HeroImageBlock(icon='image'))
    ],default='')
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

FormPage.content_panels = [
    StreamFieldPanel('body'),
    FieldPanel('intro', classname="full"),
    InlinePanel('form_fields', label="Form fields", classname='form-group'),
    FieldPanel('thank_you_text', classname="full"),
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('from_address', classname="col6"),
            FieldPanel('to_address', classname="col6"),
        ]),
        FieldPanel('subject'),
    ], "Email"),
]


class TrusteesBlock(StructBlock):
    prefix = ChoiceBlock(choices=[
        ('Dr', 'Dr.'),
        ('Mr', 'Mr.'),
        ('Mrs', 'Mrs.'),
        ('Ms', 'Ms.'),
        ])
    first_name = CharBlock()
    last_name =  CharBlock()
    title = CharBlock()
    description = RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = "trustees_block.html"


class TrusteesPage(RoutablePageMixin, Page):
    directory = StreamField([
        ('person', TrusteesBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('directory'),
    ]
    
    @route(r'^$')
    def get_context(self, value):
        context = super(TrusteesPage, self).get_context(value)
        context['dir'] = [block.value for block in self.directory]
        return render(value, 'trustees.html', context)

    @route(r'^(?P<first_name>[a-z]+)/$')
    def get_name(self, request, first_name):
        context = super(TrusteesPage, self).get_context(request)
        context['name'] = first_name
        context['names'] = [block.value for block in self.directory]
        return render(request, 'trustee.html', context)


class MediaGalleryBlock(StructBlock):
    image = ImageChooserBlock()


class Pages(Page):
    body = StreamField([
        ('single_column', SingleColumnBlock(group='COLUMNS')),
        ('two_columns', TwoColumnBlock(group='COLUMNS')),
        ('three_columns', ThreeColumnBlock(group='COLUMNS')),
        ('four_columns', FourColumnBlock(group='COLUMNS')),
        ('starfish', StarFishBlock()),
        ('trustee_page', PageChooserBlock(template='trustee_widget.html')),
        ('hero_image', HeroImageBlock(icon='image')),
        ('media_gallery', ListBlock(MediaGalleryBlock(), template='media_gallery_block.html', icon="image")),
    ],default='')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]