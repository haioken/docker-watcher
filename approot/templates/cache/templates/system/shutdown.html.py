# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.7718298
_enable_loop = True
_template_filename = 'templates/system/shutdown.html'
_template_uri = 'templates/system/shutdown.html'
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
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/system/shutdown.css?v=001" rel="stylesheet">\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/system/shutdown.js?v=002" type="text/javascript"></script>\n        <meta name="enable_notifs" content="false">\n    </head>\n    <body>\n        <div id="content" class="container-fluid">\n            <div class="message">')
        __M_writer(str(_('Shutting Down')))
        __M_writer('</div>\n            <div id="thinker">\n                <i class="mdi mdi-circle-outline animated"></i>\n            </div>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/system/shutdown.html", "line_map": {"16": 0, "32": 11, "38": 32, "24": 1, "25": 4, "26": 4, "27": 5, "28": 5, "29": 6, "30": 6, "31": 11}, "filename": "templates/system/shutdown.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
