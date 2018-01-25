# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.7829278
_enable_loop = True
_template_filename = 'templates/head.html'
_template_uri = 'templates/head.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        uitheme = context.get('uitheme', UNDEFINED)
        language = context.get('language', UNDEFINED)
        notifications = context.get('notifications', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<title>Watcher</title>\n<meta content="noindex, nofollow" name="robots">\n<meta content="')
        __M_writer(str(url_base))
        __M_writer('" name="url_base">\n<meta content="')
        __M_writer(str(language))
        __M_writer('" name="language">\n<meta content="width=device-width,initial-scale=1" name="viewport">\n\n<link rel="icon" type="image/png" href="')
        __M_writer(str(url_base))
        __M_writer('/static/images/favicon.png" />\n<link rel="apple-touch-icon" href="')
        __M_writer(str(url_base))
        __M_writer('/static/images/logo_bg.png" />\n\n<link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/themes/')
        __M_writer(str(uitheme or 'Default'))
        __M_writer('.css?v=001" rel="stylesheet">\n<link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/lib/materialdesignicons.min.css?v=001" rel="stylesheet">\n<link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/style.css?v=001" rel="stylesheet">\n\n<script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/lib/jquery.310.min.js?v=001" type="text/javascript"></script>\n<script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/lib/bootstrap.min.js?v=001" type="text/javascript"></script>\n<script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/lib/bootstrap-notify.min.js?v=001" type="text/javascript"></script>\n<script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/shared.js?v=001" type="text/javascript"></script>\n<script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/localization.js?v=001" type="text/javascript"></script>\n\n<textarea id="notifications_json" class="hidden">\n    ')
        __M_writer(str(notifications))
        __M_writer('\n</textarea>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/head.html", "line_map": {"16": 0, "25": 1, "26": 3, "27": 3, "28": 4, "29": 4, "30": 7, "31": 7, "32": 8, "33": 8, "34": 10, "35": 10, "36": 10, "37": 10, "38": 11, "39": 11, "40": 12, "41": 12, "42": 14, "43": 14, "44": 15, "45": 15, "46": 16, "47": 16, "48": 17, "49": 17, "50": 18, "51": 18, "52": 21, "53": 21, "59": 53}, "filename": "templates/head.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
