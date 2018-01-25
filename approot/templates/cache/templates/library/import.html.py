# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.3960075
_enable_loop = True
_template_filename = 'templates/library/import.html'
_template_uri = 'templates/library/import.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        navbar = context.get('navbar', UNDEFINED)
        head = context.get('head', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/library/import.css?v=001" rel="stylesheet">\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <div class="col-md-12">\n                <h1>')
        __M_writer(str(_('Import Library')))
        __M_writer('</h1>\n            </div>\n            <div class="buttons col-md-12">\n\n                <a class="btn btn-default" href="')
        __M_writer(str(url_base))
        __M_writer('/library/import/couchpotato">\n                    <img alt="CouchPotato" class="import_source_icon" src="')
        __M_writer(str(url_base))
        __M_writer('/static/images/couchpotato.png"><br>\n                    CouchPotato\n                </a>\n\n                <a class="btn btn-default" href="')
        __M_writer(str(url_base))
        __M_writer('/library/import/kodi">\n                    <img alt="Kodi" class="import_source_icon" src="')
        __M_writer(str(url_base))
        __M_writer('/static/images/kodi.png"><br>\n                    Kodi\n                </a>\n\n                <a class="btn btn-default" href="')
        __M_writer(str(url_base))
        __M_writer('/library/import/plex">\n                    <img alt="Plex" class="import_source_icon" src="')
        __M_writer(str(url_base))
        __M_writer('/static/images/plex.png"><br>\n                    Plex\n                </a>\n\n                <a class="btn btn-default" href="')
        __M_writer(str(url_base))
        __M_writer('/library/import/directory">\n                    <i class="mdi mdi-folder"></i><br>\n                    ')
        __M_writer(str(_('Directory')))
        __M_writer('\n                </a>\n            </div>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/library/import.html", "line_map": {"16": 0, "25": 1, "26": 4, "27": 4, "28": 5, "29": 5, "30": 8, "31": 8, "32": 11, "33": 11, "34": 15, "35": 15, "36": 16, "37": 16, "38": 20, "39": 20, "40": 21, "41": 21, "42": 25, "43": 25, "44": 26, "45": 26, "46": 30, "47": 30, "48": 32, "49": 32, "55": 49}, "filename": "templates/library/import.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
