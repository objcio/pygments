# -*- coding: utf-8 -*-
"""
    pygments.formatters.html
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Formatter for HTML output.

    :copyright: Copyright 2006-2015 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.formatters import HtmlFormatter

__all__ = ['ObjcioHtmlFormatter']


class ObjcioHtmlFormatter(HtmlFormatter):

    name = 'objcio'
    aliases = ['objcio']
    filenames = ['*.html', '*.htm']

    def __init__(self, **options):
        HtmlFormatter.__init__(self, **options)


    def wrap(self, source, outfile):
        return self._wrap_code(source)

    def _wrap_code(self, source):
        yield 0, '<div class="highlight"><pre><code>'
        for i, t in source:
            if i == 1:
                # it's a line of formatted code
                yield 1, t
        yield 0, '</code></pre></div>'
