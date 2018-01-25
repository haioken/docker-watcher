# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.4767787
_enable_loop = True
_template_filename = 'templates/library/stats.html'
_template_uri = 'templates/library/stats.html'
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
        __M_writer('/static/css/library/stats.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/lib/morris.css?v=001" rel="stylesheet">\n        <script type="text/javascript" src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/lib/raphael.min.js?v=06.02"></script>\n        <script type="text/javascript" src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/lib/morris.min.js?v=06.02"></script>\n        <script type="text/javascript" src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/stats.js?v=06.02"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <div id="chart_status" class="col-md-6">\n                <div class="panel panel-default">\n                    <div class="panel-heading">\n                        ')
        __M_writer(str(_('Status')))
        __M_writer('\n                    </div>\n                    <div class="chart">\n                    </div>\n                </div>\n            </div>\n            <div id="chart_profiles" class="col-md-6">\n                <div class="panel panel-default">\n                    <div class="panel-heading">\n                        ')
        __M_writer(str(_('Quality Profiles')))
        __M_writer('\n                    </div>\n                    <div class="chart">\n                    </div>\n                </div>\n            </div>\n            <div id="chart_years" class="col-md-12">\n                <div class="panel panel-default">\n                    <div class="panel-heading">\n                        ')
        __M_writer(str(_('Movies By Year')))
        __M_writer('\n                    </div>\n                    <div class="chart">\n                    </div>\n                </div>\n            </div>\n            <div id="chart_added" class="col-md-12">\n                <div class="panel panel-default">\n                    <div class="panel-heading">\n                        ')
        __M_writer(str(_('Library Growth')))
        __M_writer('\n                    </div>\n                    <div class="chart">\n                    </div>\n                </div>\n            </div>\n            <div id="chart_scores" class="col-md-12">\n                <div class="panel panel-default">\n                    <div class="panel-heading">\n                        ')
        __M_writer(str(_('Scores')))
        __M_writer('\n                    </div>\n                    <div class="chart">\n                    </div>\n                </div>\n            </div>\n        </div>\n\n        <div id="status_colors" class="hidden">\n            <span class="waiting"></span>\n            <span class="wanted"></span>\n            <span class="found"></span>\n            <span class="snatched"></span>\n            <span class="finished"></span>\n        </div>\n\n        <div id="profile_colors" class="hidden">\n            <span class="bg-primary"></span>\n            <span class="bg-success"></span>\n            <span class="bg-info"></span>\n        </div>\n\n        </textarea>\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/library/stats.html", "line_map": {"16": 0, "25": 1, "26": 4, "27": 4, "28": 5, "29": 5, "30": 6, "31": 6, "32": 7, "33": 7, "34": 8, "35": 8, "36": 9, "37": 9, "38": 12, "39": 12, "40": 17, "41": 17, "42": 26, "43": 26, "44": 35, "45": 35, "46": 44, "47": 44, "48": 53, "49": 53, "55": 49}, "filename": "templates/library/stats.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
