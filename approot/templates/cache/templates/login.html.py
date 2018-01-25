# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.8341413
_enable_loop = True
_template_filename = 'templates/login.html'
_template_uri = 'templates/login.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        uitheme = context.get('uitheme', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        <title>Watcher</title>\n        <meta content="')
        __M_writer(str(url_base))
        __M_writer('" name="url_base">\n        <meta content="width=device-width,initial-scale=1" name="viewport">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/auth/static/css/themes/')
        __M_writer(str(uitheme or 'Default'))
        __M_writer('.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/auth/static/css/lib/materialdesignicons.min.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/auth/static/css/login.css?v=001" rel="stylesheet">\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/auth/static/js/lib/jquery.310.min.js?v=001" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/auth/static/js/login.js?v=001" type="text/javascript"></script>\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/auth/static/css/style.css?v=001" rel="stylesheet">\n        <meta name="enable_notifs" content="false" />\n    </head>\n    <body>\n        <div id="content" class="container-fluid">\n            <div class="col-md-12">\n                <div class="input-group col-md-6 col-md-offset-3">\n                    <span class="input-group-addon">\n                        <i class="mdi mdi-account"></i>\n                    </span>\n                    <input type="text" id="user" class="form-control">\n                </div>\n            </div>\n            <div class="col-md-12">\n                <div class="input-group col-md-6 col-md-offset-3">\n                    <span class="input-group-addon">\n                        <i class="mdi mdi-lock"></i>\n                    </span>\n                    <input type="password" id="password" class="form-control">\n                </div>\n            </div>\n            <div class="col-md-12 col-sm-12">\n                <div class="input-group col-md-6 col-md-offset-3 col-sm-12">\n                    <a class="message btn btn-primary" onclick="login(event)">\n                        <i class="mdi mdi-login"></i>\n                    </a>\n                </div>\n            </div>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/login.html", "line_map": {"32": 9, "33": 9, "34": 10, "35": 10, "36": 11, "37": 11, "38": 12, "39": 12, "45": 39, "16": 0, "23": 1, "24": 5, "25": 5, "26": 7, "27": 7, "28": 7, "29": 7, "30": 8, "31": 8}, "filename": "templates/login.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
