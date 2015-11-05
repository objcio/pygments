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

    name = 'OBJCIO'
    aliases = ['objcio']
    filenames = ['*.html', '*.htm']

    def __init__(self, **options):
        HtmlFormatter.__init__(self, **options)
        self.inputIndent = int(options.get('input-indent', '4'))
        self.indent = int(options.get('indent', '3'))


    def wrap(self, source, outfile):
        return self._wrap_code(source)

    def _wrap_code(self, source):
        yield 0, '<div class="code">'
        format = '<div class="line" style="padding-left:{0}ch;margin-left:{2}ch;text-indent:-{2}ch;">{1}</div>'
        for i, t in source:
            if i == 1:
                # it's a line of formatted code
                trimmedLine = t.lstrip()
                diff = len(t) - len(trimmedLine)
                yield 1, format.format(self.indent * diff/self.inputIndent, trimmedLine, self.indent)
        yield 0, '</div>'
