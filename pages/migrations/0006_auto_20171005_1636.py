# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 16:36
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20171005_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('single_column', wagtail.wagtailcore.blocks.StructBlock((('column', wagtail.wagtailcore.blocks.StreamBlock((('h1', wagtail.wagtailcore.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('lead_body', wagtail.wagtailcore.blocks.CharBlock(classname='lead')), ('small_text', wagtail.wagtailcore.blocks.CharBlock(classname='small')), ('blockquote', wagtail.wagtailcore.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('icon', wagtail.wagtailcore.blocks.StructBlock((('font_awesome_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('background_color', pages.models.BackgroundColorBlock())), group='COLUMNS')), ('two_columns', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('h1', wagtail.wagtailcore.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('lead_body', wagtail.wagtailcore.blocks.CharBlock(classname='lead')), ('small_text', wagtail.wagtailcore.blocks.CharBlock(classname='small')), ('blockquote', wagtail.wagtailcore.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('icon', wagtail.wagtailcore.blocks.StructBlock((('font_awesome_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('h1', wagtail.wagtailcore.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('lead_body', wagtail.wagtailcore.blocks.CharBlock(classname='lead')), ('small_text', wagtail.wagtailcore.blocks.CharBlock(classname='small')), ('blockquote', wagtail.wagtailcore.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('icon', wagtail.wagtailcore.blocks.StructBlock((('font_awesome_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('background_color', pages.models.BackgroundColorBlock())), group='COLUMNS')), ('four_columns', wagtail.wagtailcore.blocks.StructBlock((('left_column_1', wagtail.wagtailcore.blocks.StreamBlock((('h1', wagtail.wagtailcore.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('lead_body', wagtail.wagtailcore.blocks.CharBlock(classname='lead')), ('small_text', wagtail.wagtailcore.blocks.CharBlock(classname='small')), ('blockquote', wagtail.wagtailcore.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('icon', wagtail.wagtailcore.blocks.StructBlock((('font_awesome_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('left_column_2', wagtail.wagtailcore.blocks.StreamBlock((('h1', wagtail.wagtailcore.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('lead_body', wagtail.wagtailcore.blocks.CharBlock(classname='lead')), ('small_text', wagtail.wagtailcore.blocks.CharBlock(classname='small')), ('blockquote', wagtail.wagtailcore.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('icon', wagtail.wagtailcore.blocks.StructBlock((('font_awesome_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('right_column_1', wagtail.wagtailcore.blocks.StreamBlock((('h1', wagtail.wagtailcore.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('lead_body', wagtail.wagtailcore.blocks.CharBlock(classname='lead')), ('small_text', wagtail.wagtailcore.blocks.CharBlock(classname='small')), ('blockquote', wagtail.wagtailcore.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('icon', wagtail.wagtailcore.blocks.StructBlock((('font_awesome_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('right_column_2', wagtail.wagtailcore.blocks.StreamBlock((('h1', wagtail.wagtailcore.blocks.CharBlock(classname='title', help_text='Always use only one H1 per page')), ('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('lead_body', wagtail.wagtailcore.blocks.CharBlock(classname='lead')), ('small_text', wagtail.wagtailcore.blocks.CharBlock(classname='small')), ('blockquote', wagtail.wagtailcore.blocks.CharBlock(classname='blockquote')), ('pull_quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('icon', wagtail.wagtailcore.blocks.StructBlock((('font_awesome_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('font_awesome_icon_size', pages.models.FontAwesomeIconSizeBlock()), ('material_icon_name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('material_icon_size', pages.models.MaterialIconSizeBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')]))))), ('raw_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right'), ('text-justify', 'Justify'), ('text-nowrap', 'No Wrap')])))))))), ('background_color', pages.models.BackgroundColorBlock())), group='COLUMNS')), ('starfish', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()),))), ('hero_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('alternate_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Text for screen readers')), ('caption', wagtail.wagtailcore.blocks.CharBlock(help_text='Caption will be shown below the image', max_length=120, required=False)), ('fine_print', wagtail.wagtailcore.blocks.CharBlock(help_text='Fine Print will be shown below caption', max_length=120, required=False)), ('overlay_text', wagtail.wagtailcore.blocks.BooleanBlock(help_text='If checked, caption is overlayed on image', required=False)), ('photo_credit', wagtail.wagtailcore.blocks.CharBlock(help_text='This will show bottom right on the image', max_length=80, required=False))), icon='image'))), default=''),
        ),
    ]
