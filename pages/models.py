from django.db import models
from django.shortcuts import render

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.contrib.forms.models import AbstractFormField

from wagtailcaptcha.forms import WagtailCaptchaFormBuilder
from wagtailcaptcha.models import WagtailCaptchaEmailForm

from .blocks import (
    SingleColumnBlock,
    TwoColumnBlock,
    ThreeColumnBlock,
    FourColumnBlock,
    ImageGridBlock,
    StarFishBlock,
    PageChooserBlock,
    ListBlock,
    MediaGalleryBlock,
    TrusteesBlock,
)

from modelcluster.fields import ParentalKey


class FormField(AbstractFormField):
    page = ParentalKey("FormPage", related_name="form_fields")


class CaptchaV3FormBuilder(WagtailCaptchaFormBuilder):
    @property
    def formfields(self):
        fields = super(WagtailCaptchaFormBuilder, self).formfields
        fields[self.CAPTCHA_FIELD_NAME] = ReCaptchaField(
            label="", widget=ReCaptchaV3(action="form-submit")
        )
        return fields


class FormPage(WagtailCaptchaEmailForm):
    form_builder = CaptchaV3FormBuilder
    # Hero section of Page
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="2400X858px",
    )
    hero_heading = models.CharField(
        null=True, blank=True, max_length=140, help_text="40 character limit."
    )
    hero_caption = models.CharField(
        null=True, blank=True, max_length=140, help_text="140 character limit."
    )
    hero_photo_credit = models.CharField(
        null=True,
        blank=True,
        max_length=80,
        help_text="80 character limit. \
                   This will show on the bottom right on the image",
    )
    hero_photo_credit_link = models.URLField(
        null=True,
        blank=True,
        help_text="If you would like the above text\
                   to link to a website. Enter complete URL here.",
    )
    hero_cta = models.CharField(
        null=True,
        blank=True,
        verbose_name="Hero CTA",
        max_length=20,
        help_text="Text to display on Call to Action. 20 character limit.",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link the Call to Action",
    )
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)


FormPage.content_panels = [
    MultiFieldPanel(
        [
            FieldPanel("hero_image"),
            FieldPanel("hero_heading", classname="full"),
            FieldPanel("hero_caption", classname="full"),
            FieldPanel("hero_photo_credit", classname="full"),
            FieldPanel("hero_photo_credit_link", classname="full"),
            MultiFieldPanel(
                [
                    FieldPanel("hero_cta"),
                    FieldPanel("hero_cta_link"),
                ]
            ),
        ],
        heading="Hero Image",
    ),
    FieldPanel("title", classname="full"),
    FieldPanel("intro", classname="full"),
    InlinePanel("form_fields", label="Form fields", classname="form-group"),
    FieldPanel("thank_you_text", classname="full"),
    MultiFieldPanel(
        [
            FieldRowPanel(
                [
                    FieldPanel("from_address", classname="col6"),
                    FieldPanel("to_address", classname="col6"),
                ]
            ),
            FieldPanel("subject"),
        ],
        "Email",
    ),
]


class StandardPage(Page):
    # Hero section of Page
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="2400X858px",
    )
    hero_heading = models.CharField(
        null=True, blank=True, max_length=140, help_text="40 character limit."
    )
    hero_caption = models.CharField(
        null=True, blank=True, max_length=140, help_text="140 character limit."
    )
    hero_photo_credit = models.CharField(
        null=True,
        blank=True,
        max_length=80,
        help_text="80 character limit. This will show\
                   on the bottom right on the image",
    )
    hero_photo_credit_link = models.URLField(
        null=True,
        blank=True,
        help_text="If you would like the above text\
                   to link to a website. Enter complete URL here.",
    )
    hero_cta = models.CharField(
        null=True,
        blank=True,
        verbose_name="Hero CTA",
        max_length=20,
        help_text="Text to display on Call to Action. 20 character limit.",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link the Call to Action",
    )
    body = StreamField(
        [
            ("single_column", SingleColumnBlock(group="COLUMNS")),
            ("two_columns", TwoColumnBlock(group="COLUMNS")),
            ("three_columns", ThreeColumnBlock(group="COLUMNS")),
            ("four_columns", FourColumnBlock(group="COLUMNS")),
            (
                "image_grid",
                ImageGridBlock(
                    icon="image",
                    min_num=2,
                    max_num=4,
                    help_text="Minimum 2 blocks and a maximum of 4 blocks",
                ),
            ),
            ("starfish", StarFishBlock()),
            ("trustee_page", PageChooserBlock(template="trustee_widget.html")),
            (
                "media_gallery",
                ListBlock(
                    MediaGalleryBlock(),
                    template="blocks/media_gallery_block.html",
                    icon="image",
                ),
            ),
        ],
        use_json_field=True,
        default="",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_image"),
                FieldPanel("hero_heading", classname="full"),
                FieldPanel("hero_caption", classname="full"),
                FieldPanel("hero_photo_credit", classname="full"),
                FieldPanel("hero_photo_credit_link", classname="full"),
                MultiFieldPanel(
                    [
                        FieldPanel("hero_cta"),
                        FieldPanel("hero_cta_link"),
                    ]
                ),
            ],
            heading="Hero Image",
        ),
        FieldPanel("body"),
    ]


class TrusteesPage(RoutablePageMixin, Page):
    directory = StreamField([("person", TrusteesBlock())], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("directory"),
    ]

    @route(r"^$")
    def get_context(self, value):
        context = super(TrusteesPage, self).get_context(value)
        context["dir"] = [block.value for block in self.directory]
        return render(value, "trustees.html", context)

    @route(r"^(?P<first_name>[a-z]+)/$")
    def get_name(self, request, first_name):
        context = super(TrusteesPage, self).get_context(request)
        context["name"] = first_name
        context["names"] = [block.value for block in self.directory]
        return render(request, "trustee.html", context)
