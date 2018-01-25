# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.7791948
_enable_loop = True
_template_filename = 'templates/404.html'
_template_uri = 'templates/404.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        head = context.get('head', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/404.css?v=001" rel="stylesheet">\n        <meta name="enable_notifs" content="false" />\n    </head>\n    <body>\n        <div id="content" class="container-fluid navbar-default">\n            <div class="message invert">\n                404<br/>\n                ')
        __M_writer(str(_('Page Not Found')))
        __M_writer('\n            </div>\n        </div>\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/404.html", "line_map": {"16": 0, "36": 30, "24": 1, "25": 5, "26": 5, "27": 6, "28": 6, "29": 13, "30": 13}, "filename": "templates/404.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
