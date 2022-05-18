# Generated by Django 4.0.4 on 2022-05-18 22:41

from django.db import migrations, models
import pages.blocks
import wagtail.blocks
import wagtail.contrib.forms.models
import wagtail.contrib.table_block.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_formfield_clean_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='choices',
            field=models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='default_value',
            field=models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value'),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='from_address',
            field=models.EmailField(blank=True, max_length=255, verbose_name='from address'),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='to_address',
            field=models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address'),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.fields.StreamField([('single_column', wagtail.blocks.StructBlock([('column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('two_columns', wagtail.blocks.StructBlock([('left_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('three_columns', wagtail.blocks.StructBlock([('left_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('middle_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('four_columns', wagtail.blocks.StructBlock([('left_column_1', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('left_column_2', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column_1', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column_2', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('image_grid', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))], help_text='Minimum 2 blocks and a maximum of 4 blocks', icon='image', max_num=4, min_num=2)), ('starfish', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock())])), ('trustee_page', wagtail.blocks.PageChooserBlock(template='trustee_widget.html')), ('media_gallery', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())]), icon='image', template='blocks/media_gallery_block.html'))], default='', use_json_field=True),
        ),
        migrations.AlterField(
            model_name='trusteespage',
            name='directory',
            field=wagtail.fields.StreamField([('person', wagtail.blocks.StructBlock([('prefix', wagtail.blocks.ChoiceBlock(choices=[('Dr', 'Dr.'), ('Mr', 'Mr.'), ('Mrs', 'Mrs.'), ('Ms', 'Ms.')])), ('first_name', wagtail.blocks.CharBlock()), ('last_name', wagtail.blocks.CharBlock()), ('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))], use_json_field=True),
        ),
    ]
