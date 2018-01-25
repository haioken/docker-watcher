# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.4138088
_enable_loop = True
_template_filename = 'templates/library/import/couchpotato.html'
_template_uri = 'templates/library/import/couchpotato.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        head = context.get('head', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        profiles = context.get('profiles', UNDEFINED)
        sources = context.get('sources', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/library/import/couchpotato.css?v=001" rel="stylesheet">\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/import/shared.js?v=001" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/import/couchpotato.js?v=002" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <h1>')
        __M_writer(str(_('Import CouchPotato Library')))
        __M_writer('</h1>\n            <br/>\n            <span id="progress_text"></span>\n            <div class="progress hidden">\n                <div class="progress-bar"></div>\n            </div>\n\n            <div id="server_info" class="panel panel-default">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('CouchPotato Server Information')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('Address')))
        __M_writer('</label>\n                        <input type="text" id="address" class="form-control" placeholder="http://localhost">\n                    </div>\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('Port')))
        __M_writer('</label>\n                        <input type="number" id="port" class="form-control" min="0" placeholder="5050">\n                    </div>\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('API Key')))
        __M_writer('</label>\n                        <input type="text" id="apikey" class="form-control" placeholder="123456789abcdef">\n                    </div>\n                </div>\n            </div>\n            <a id="scan_library" class="btn btn-primary" onclick="scan_library(event, this)">\n                <i class="mdi mdi-file-find"></i>\n                ')
        __M_writer(str(_('Scan Library')))
        __M_writer('\n            </a>\n\n            <div id="no_new_movies" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('No New Movies Found')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    ')
        __M_writer(str(_('No new movies have been found in CouchPotato\'s library.')))
        __M_writer('\n                </div>\n            </div>\n\n            <div id="wanted_movies" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Wanted Movies')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <table class="table table-striped table-hover">\n                        <thead>\n                            <tr>\n                                <th class="shrink">')
        __M_writer(str(_('Import')))
        __M_writer('</th>\n                                <th>')
        __M_writer(str(_('Title')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('IMDB ID')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('Quality&nbsp;Profile')))
        __M_writer('</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                        </tbody>\n                    </table>\n                </div>\n            </div>\n\n            <div id="finished_movies" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Finished Movies')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <table class="table table-striped table-hover">\n                        <thead>\n                            <tr>\n                                <th class="shrink">')
        __M_writer(str(_('Import')))
        __M_writer('</th>\n                                <th>')
        __M_writer(str(_('Title')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('IMDB ID')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('Source')))
        __M_writer('</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                        </tbody>\n                    </table>\n                </div>\n            </div>\n\n            <a id="import_library" class="btn btn-primary hidden" onclick="import_library(event, this)">\n                <i class="mdi mdi-archive"></i>\n                ')
        __M_writer(str(_('Import Library')))
        __M_writer('\n            </a>\n\n\n            <div id="import_success" class="panel panel-success hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Imported Movies')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <table class="table table-striped table-hover">\n                        <thead>\n                            <tr>\n                                <th>')
        __M_writer(str(_('Title')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('IMDB ID')))
        __M_writer('</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                        </tbody>\n                    </table>\n                </div>\n            </div>\n\n            <div id="import_error" class="panel panel-danger hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Import Errors')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <table class="table table-striped table-hover">\n                        <thead>\n                            <tr>\n                                <th>')
        __M_writer(str(_('Title')))
        __M_writer('</th>\n                                <th>')
        __M_writer(str(_('Error')))
        __M_writer('</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                        </tbody>\n                    </table>\n                </div>\n            </div>\n\n            <a id="import_return" class="btn btn-success hidden" href="')
        __M_writer(str(url_base))
        __M_writer('/library/import">\n                <i class="mdi mdi-undo-variant"></i>\n                ')
        __M_writer(str(_('Return')))
        __M_writer('\n            </a>\n\n\n        </div>\n        <textarea id="source_select" class="hidden">\n            <select class="source_select btn btn-sm btn-default">\n')
        for source in sources:
            __M_writer('                <option value="')
            __M_writer(str(source))
            __M_writer('">')
            __M_writer(str(source))
            __M_writer('</option>\n')
        __M_writer('            </select>\n        </textarea>\n        <textarea id="quality_select" class="hidden">\n            <select class="quality_select btn btn-sm btn-default">\n')
        for profile in profiles:
            if profile == "Default":
                __M_writer('                    <option value="Default" selected="true">Default</option>\n')
            else:
                __M_writer('                    <option value="')
                __M_writer(str(profile))
                __M_writer('">')
                __M_writer(str(profile))
                __M_writer('</option>\n')
        __M_writer('            </select>\n        </textarea>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/library/import/couchpotato.html", "line_map": {"16": 0, "27": 1, "28": 4, "29": 4, "30": 5, "31": 5, "32": 6, "33": 6, "34": 7, "35": 7, "36": 10, "37": 10, "38": 12, "39": 12, "40": 21, "41": 21, "42": 25, "43": 25, "44": 29, "45": 29, "46": 33, "47": 33, "48": 40, "49": 40, "50": 45, "51": 45, "52": 48, "53": 48, "54": 54, "55": 54, "56": 60, "57": 60, "58": 61, "59": 61, "60": 62, "61": 62, "62": 63, "63": 63, "64": 74, "65": 74, "66": 80, "67": 80, "68": 81, "69": 81, "70": 82, "71": 82, "72": 83, "73": 83, "74": 94, "75": 94, "76": 100, "77": 100, "78": 106, "79": 106, "80": 107, "81": 107, "82": 118, "83": 118, "84": 124, "85": 124, "86": 125, "87": 125, "88": 134, "89": 134, "90": 136, "91": 136, "92": 143, "93": 144, "94": 144, "95": 144, "96": 144, "97": 144, "98": 146, "99": 150, "100": 151, "101": 152, "102": 153, "103": 154, "104": 154, "105": 154, "106": 154, "107": 154, "108": 157, "114": 108}, "filename": "templates/library/import/couchpotato.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
