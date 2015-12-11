# -*- coding: utf-8 -*-
"""
    pygments.formatters.html
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Formatter for HTML output.

    :copyright: Copyright 2006-2015 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.formatters import HtmlFormatter

__all__ = ['ObjcioEpubHtmlFormatter']


class ObjcioEpubHtmlFormatter(HtmlFormatter):

    name = 'objcio-epub'
    aliases = ['objcio-epub']
    filenames = ['*.html', '*.htm']

    def __init__(self, **options):
        HtmlFormatter.__init__(self, **options)
        self.inputIndent = int(options.get('input-indent', '4'))
        self.indent = float(options.get('indent', '3'))
        self.indentUnit = options.get('indent-unit', 'ch')


    def wrap(self, source, outfile):
        return self._wrap_code(source)

    def _wrap_code(self, source):
        yield 0, '<div class="code">'
        format = '<div class="line" style="padding-left:{0}{3};margin-left:{2}{3};text-indent:-{2}{3};">{1}</div>'
        for i, t in source:
            if i == 1:
                # it's a line of formatted code
                trimmedLine = t.lstrip()
                diff = len(t) - len(trimmedLine)
                yield 1, format.format(self.indent * diff/self.inputIndent, trimmedLine, self.indent, self.indentUnit)
        yield 0, '</div>'
