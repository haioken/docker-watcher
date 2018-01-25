# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.7767818
_enable_loop = True
_template_filename = 'templates/system/update.html'
_template_uri = 'templates/system/update.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        head = context.get('head', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        updating = context.get('updating', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/system/update.css?v=001" rel="stylesheet">\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/system/update.js?v=003" type="text/javascript"></script>\n        <meta name="enable_notifs" content="false">\n        <meta name="updating" content="')
        __M_writer(str(updating))
        __M_writer('">\n    </head>\n    <body>\n        <div id="content" class="container-fluid">\n\n            <div class="tasks hidden">\n                <h4>')
        __M_writer(str(_('Waiting for tasks to finish...')))
        __M_writer('</h4>\n\n            </div>\n\n\n            <div class="updating hidden">')
        __M_writer(str(_('Updating')))
        __M_writer('</div>\n            <div id="thinker">\n                <i class="mdi mdi-circle-outline animated"></i>\n            </div>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/system/update.html", "line_map": {"32": 8, "33": 8, "34": 14, "35": 14, "36": 19, "37": 19, "43": 37, "16": 0, "25": 1, "26": 4, "27": 4, "28": 5, "29": 5, "30": 6, "31": 6}, "filename": "templates/system/update.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
