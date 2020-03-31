

import re
import os
import subprocess



# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo',
    'sphinx.ext.autosummary', 'toolkit_sphinx_extension',]
autodoc_member_order = 'bysource'
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8'
latex_engine = 'xelatex'
# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'Open Data documentation'
project_short_name = u'opendata'
copyright = u'''Copyright VNPT INFORMATION TECHNOLOGY COMPANY'''
html_show_sphinx = False


version = u''
# The full version, including alpha/beta/rc tags.
release =  u'1.0'
version_re = None
point_releases_ = None

exclude_trees = ['.build']


pygments_style = 'sphinx'


# Options for HTML output
# -----------------------

extra_css_files = ['_static/css/custom.css']

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_sidebars = {
    '**':  ['globaltoc.html'],
}


html_static_path = ['_static']


htmlhelp_basename = 'OpenDatadoc'


latex_documents = [
  ('contents', 'Opendata.tex', u'Open Data documentation',
   u'Opendata contributors', 'manual'),
]

