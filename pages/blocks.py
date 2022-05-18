from django import forms

from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.blocks import (
    BooleanBlock, CharBlock, ChoiceBlock, FieldBlock, ListBlock, PageChooserBlock, RawHTMLBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock, URLBlock
)
from wagtail.contrib.table_block.blocks import TableBlock


class AlignmentBlock(ChoiceBlock):
    choices = [
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right')
    ]

    # Returning CSS Framework classes
    def get_alignment_class(self):
        if self == 'left':
            return 'start'
        elif self == 'center':
            return 'center'
        elif self == 'right':
            return 'end'


class AlignedRAWHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = AlignmentBlock(default='left')

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        # Context for adding Bootstrap class variable
        context['alignment_class'] = AlignmentBlock.get_alignment_class(value['alignment'])
        return context
        
    class Meta:
        template = 'blocks/aligned_raw_html_block.html'


class BackgroundColorBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), 
        ('white-smoke', 'White Smoke'),
        ('aqua-island', 'Aqua Island'),
        ('concrete', 'Concrete')
    ))


class ButtonBlock(StructBlock):
    alignment = AlignmentBlock(default='left')
    size = ChoiceBlock([
        ('sm', 'Small'),
        ('md', 'Medium'),
        ('lg', 'Large')
    ])
    cta_text = CharBlock(max_length=25, help_text='25 character limit.')
    internal_link = PageChooserBlock(required=False)
    external_link = URLBlock(required=False)
    color = ChoiceBlock([
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('dark-brown', 'Dark Brown'),
        ('white-smoke', 'White Smoke'),
        ('concrete', 'Concrete'),
        ('aqua-island', 'Aqua Island'),

    ])

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        # Context for adding Bootstrap class variable
        context['alignment_class'] = AlignmentBlock.get_alignment_class(value['alignment'])
        return context

    class Meta:
        icon = 'pick'
        template = 'blocks/button_block.html'


class IconBlock(StructBlock):
    icon = ChoiceBlock([
        ('font-awesome', 'Font Awesome'),
        ('material-icon', 'Material Icon')
    ])
    name = CharBlock(max_length=25, help_text='25 character limit')
    size = ChoiceBlock(choices = [
        ('sm', 'Small'),
        ('md', 'Medium'),
        ('lg', 'Large'),
        ('xl', 'Extra Large')
    ])
    font_awesome_icon_choice = ChoiceBlock([
        ('solid', 'Solid'),
        ('regular', 'Regular'),
        ('light', 'Light'),
        ('brand', 'Brand')
    ], required=False)
    alignment = AlignmentBlock(default='left')

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        # Context for adding Bootstrap class variable
        context['alignment_class'] = AlignmentBlock.get_alignment_class(value['alignment'])
        return context

    class Meta:
        icon = 'wagtail'
        template = 'blocks/icon_block.html'


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    alignment = AlignmentBlock(default='left', required=False)
    border = BooleanBlock(required=False, help_text='Adds border around image')

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        # Context for adding Bootstrap class variable
        context['alignment_class'] = AlignmentBlock.get_alignment_class(value['alignment'])
        return context

    class Meta:
        icon = 'image'
        template = 'blocks/image_block.html'


class ImageGridBlock(StreamBlock):
    grid = StructBlock([
        ('image', ImageChooserBlock(required=True, help_text='size: 800X450px')),
        ('caption', CharBlock(max_length=26, help_text='26 characters limit')),
        ('description', CharBlock(max_length=300, required=False, help_text='300 characters limit')),
        ('link', PageChooserBlock(required=False))
    ])

    class Meta:
        icon = 'image'
        template = 'blocks/image_grid_block.html'


class MediaGalleryBlock(StructBlock):
    image = ImageChooserBlock()


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h6 sizes for headers
    """
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h1', 'H1'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
        ('h6', 'H6')
    ], blank=True, required=False)
    alignment = AlignmentBlock(default='left', required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        # Context for adding Bootstrap class variable
        context['alignment_class'] = AlignmentBlock.get_alignment_class(value['alignment'])
        return context

    class Meta:
        icon = 'pilcrow'
        template = 'blocks/heading_block.html'


class StarFishBlock(StructBlock):
    html = RawHTMLBlock()

    class Meta:
        template = 'blocks/starfish_block.html'
        label = 'Starfish'


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon='pilcrow',
        template='blocks/paragraph_block.html'
    )
    image_block = ImageBlock()
    document = DocumentChooserBlock(icon='doc-full-inverse')
    button_block = ButtonBlock()
    image_grid_block = ImageGridBlock()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='code',
        template='blocks/embed_block.html')
    icon_block = IconBlock()
    table = TableBlock(template='includes/table.html')
    raw_html = AlignedRAWHTMLBlock()


class SingleColumnBlock(StructBlock):
    column = BaseStreamBlock()
    alignment = AlignmentBlock(default='left')
    background_color = BackgroundColorBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        # Context for adding Bootstrap class variable
        context['alignment_class'] = AlignmentBlock.get_alignment_class(value['alignment'])
        return context

    class Meta:
        label = 'Single Column'
        template = 'blocks/single_column_block.html'


class TwoColumnBlock(StructBlock):
    left_column = BaseStreamBlock()
    right_column = BaseStreamBlock()
    alignment = AlignmentBlock(default='left')
    background_color = BackgroundColorBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        # Context for adding Bootstrap class variable
        context['alignment_class'] = AlignmentBlock.get_alignment_class(value['alignment'])
        return context

    class Meta:
        label = 'Two Columns'
        template = 'blocks/two_column_block.html'


class ThreeColumnBlock(StructBlock):
    left_column = BaseStreamBlock()
    middle_column = BaseStreamBlock()
    right_column = BaseStreamBlock()
    alignment = AlignmentBlock(default='left')
    background_color = BackgroundColorBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        # Context for adding Bootstrap class variable
        context['alignment_class'] = AlignmentBlock.get_alignment_class(value['alignment'])
        return context

    class Meta:
        label = 'Three Columns'
        template = 'blocks/three_column_block.html'


class FourColumnBlock(StructBlock):
    left_column_1 = BaseStreamBlock()
    left_column_2 = BaseStreamBlock()
    right_column_1 = BaseStreamBlock()
    right_column_2 = BaseStreamBlock()
    alignment = AlignmentBlock(default='left')
    background_color = BackgroundColorBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        # Context for adding Bootstrap class variable
        context['alignment_class'] = AlignmentBlock.get_alignment_class(value['alignment'])
        return context

    class Meta:
        label = 'Four Columns'
        template = 'blocks/four_column_block.html'


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
        template = "blocks/trustees_block.html"