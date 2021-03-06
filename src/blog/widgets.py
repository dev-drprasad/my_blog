from django import forms
from django.utils.html import escape
from django.utils.safestring import mark_safe


class MarkdownEditor(forms.Widget):
    """
    Code Editor built upon Javascript editor:CodeMirror
    """
    class Media:
        css = {
            'all': (
                'codemirror/codemirror.css',
                'codemirror/mdn-like.css',
            )
        }

        js = (
            'codemirror/codemirror.js',
            'codemirror/mode/markdown/markdown.js',
        )

    def render(self, name, value, attrs=None, renderer=None):

        template = '''
            <textarea name="%(name)s" id="id_%(name)s" required="" class="vLargeTextField">%(value)s</textarea>
            <style>
                .CodeMirror {
                    height: auto;
                }
                .CodeMirror-scroll {
                    min-height: 300px;
                }
            </style>
            <script>
                var editorElem = document.querySelector("#id_%(name)s");
                var editor = CodeMirror.fromTextArea(editorElem, {
                    lineWrapping: true,
                    theme: 'mdn-like',
                    lineNumbers: true,
                });
            </script>
        '''
        context = {'name': name, 'value': escape(value) if value else ''}
        return mark_safe(template % context)
