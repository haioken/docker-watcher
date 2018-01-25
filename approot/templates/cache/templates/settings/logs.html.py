# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.747986
_enable_loop = True
_template_filename = 'templates/settings/logs.html'
_template_uri = 'templates/settings/logs.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        logfiles = context.get('logfiles', UNDEFINED)
        head = context.get('head', UNDEFINED)
        logdir = context.get('logdir', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/shared.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/log.css?v=001" rel="stylesheet">\n\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/shared.js?v=002" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/logs.js?v=002" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <h1>')
        __M_writer(str(_('Logs')))
        __M_writer('</h1>\n\n            <div class="well">\n                <div class="col-md-12 ">\n                        <label>')
        __M_writer(str(_('Log Directory')))
        __M_writer('</label>\n                        <span class="list-group-item">')
        __M_writer(str(logdir))
        __M_writer('</span>\n                </div>\n\n                <div class="col-md-12">\n                    <label>')
        __M_writer(str(_('Log Files')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <select id="log_file" class="form-control">\n')
        for log in logfiles:
            __M_writer('                            <option value="')
            __M_writer(str(log))
            __M_writer('">')
            __M_writer(str(log))
            __M_writer('</option>\n')
        __M_writer('                        </select>\n                        <span class="input-group-btn">\n                            <a id="view" class="btn btn-info" onclick="view_log()">\n                                <i class="mdi mdi-clipboard-text"></i>\n                                ')
        __M_writer(str(_('View')))
        __M_writer('\n                            </a>\n                        </span>\n                        <span class="input-group-btn">\n                            <a class="btn btn-primary" onclick="download_log()">\n                                <i class="mdi mdi-download"></i>\n                                ')
        __M_writer(str(_('Download')))
        __M_writer('\n                            </a>\n                        </span>\n                    </div>\n                </div>\n            </div>\n\n            <pre id="log_text" class="hidden"></pre>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/settings/logs.html", "line_map": {"64": 58, "16": 0, "27": 1, "28": 4, "29": 4, "30": 5, "31": 5, "32": 6, "33": 6, "34": 8, "35": 8, "36": 9, "37": 9, "38": 12, "39": 12, "40": 14, "41": 14, "42": 18, "43": 18, "44": 19, "45": 19, "46": 23, "47": 23, "48": 26, "49": 27, "50": 27, "51": 27, "52": 27, "53": 27, "54": 29, "55": 33, "56": 33, "57": 39, "58": 39}, "filename": "templates/settings/logs.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
