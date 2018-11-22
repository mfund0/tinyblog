import mistune
from pygments.formatters import html
from pygments import highlight
from pygments.lexers import get_lexer_by_name

class Renderer(mistune.Renderer):

    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code><blockquotes>%s</blockquotes></code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)
