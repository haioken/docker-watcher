# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.4316568
_enable_loop = True
_template_filename = 'templates/library/import/kodi.html'
_template_uri = 'templates/library/import/kodi.html'
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
        __M_writer('/static/css/library/import/kodi.css?v=001" rel="stylesheet">\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/import/shared.js?v=001" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/import/kodi.js?v=001" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <h1>')
        __M_writer(str(_('Import Kodi Library')))
        __M_writer('</h1>\n            <br/>\n            <span id="progress_text"></span>\n            <div class="progress hidden">\n                <div class="progress-bar"></div>\n            </div>\n\n            <div id="server_info" class="panel panel-default">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Kodi Server Information')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('Address')))
        __M_writer('</label>\n                        <input type="text" id="address" class="form-control" placeholder="http://localhost">\n                    </div>\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('Port')))
        __M_writer('</label>\n                        <input type="number" id="port" class="form-control" min="0" placeholder="8080">\n                    </div>\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('User Name')))
        __M_writer('</label>\n                        <input type="text" id="user" class="form-control" placeholder="Kodi">\n                    </div>\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('Password')))
        __M_writer('</label>\n                        <input type="text" id="password" class="form-control" placeholder="password">\n                    </div>\n                </div>\n            </div>\n            <a id="scan_library" class="btn btn-primary" onclick="scan_library(event, this)">\n                <i class="mdi mdi-file-find"></i>\n                ')
        __M_writer(str(_('Scan Library')))
        __M_writer('\n            </a>\n\n            <div id="no_new_movies" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('No New Movies Found')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    ')
        __M_writer(str(_('No new movies have been found in Kodi\'s library.')))
        __M_writer('\n                </div>\n            </div>\n\n            <div id="remote_map" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Remote Paths')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <p>')
        __M_writer(str(_('Kodi lists file locations relative to itself. If Kodi is on a different device than Watcher you may need to alter file paths.')))
        __M_writer('\n                    </p>\n                    <p>\n                        ')
        __M_writer(str(_('To alter a remote path, enter the information in the following form and click Apply. Multiple changes can be applied. Use the same principles as described in the wiki.')))
        __M_writer('\n                        <a href="https://github.com/nosmokingbandit/Watcher3/wiki/Remote-Mapping" target="_blank" rel="noopener">\n                            <i class="mdi mdi-help-circle-outline"></i>\n                        </a>\n                    </p>\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('Local Path')))
        __M_writer('</label>\n                        <input type="text" id="local_path" class="form-control" placeholder="//Movies">\n                    </div>\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('Remote Path')))
        __M_writer('</label>\n                        <input type="text" id="remote_path" class="form-control" placeholder="//Movies">\n                    </div>\n                    <div id="remote_actions" class="col-md-6 btn-group">\n                        <a class="btn btn-default" onclick="apply_remote(event)">\n                            <i class="mdi mdi-check"></i>\n                            ')
        __M_writer(str(_('Apply')))
        __M_writer('\n                        </a>\n                        <a class="btn btn-default" onclick="reset_remote(event)">\n                            <i class="mdi mdi-undo"></i>\n                            ')
        __M_writer(str(_('Reset')))
        __M_writer('\n                        </a>\n                    </div>\n                </div>\n            </div>\n\n            <div id="scanned_movies" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Kodi Movies')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <table class="table table-striped table-hover">\n                        <thead>\n                            <tr>\n                                <th class="shrink">')
        __M_writer(str(_('Import')))
        __M_writer('</th>\n                                <th>')
        __M_writer(str(_('File Location')))
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
        __M_writer('            </select>\n        </textarea>\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/library/import/kodi.html", "line_map": {"16": 0, "27": 1, "28": 4, "29": 4, "30": 5, "31": 5, "32": 6, "33": 6, "34": 7, "35": 7, "36": 10, "37": 10, "38": 12, "39": 12, "40": 21, "41": 21, "42": 25, "43": 25, "44": 29, "45": 29, "46": 33, "47": 33, "48": 37, "49": 37, "50": 44, "51": 44, "52": 49, "53": 49, "54": 52, "55": 52, "56": 58, "57": 58, "58": 61, "59": 61, "60": 64, "61": 64, "62": 70, "63": 70, "64": 74, "65": 74, "66": 80, "67": 80, "68": 84, "69": 84, "70": 92, "71": 92, "72": 98, "73": 98, "74": 99, "75": 99, "76": 100, "77": 100, "78": 101, "79": 101, "80": 102, "81": 102, "82": 113, "83": 113, "84": 119, "85": 119, "86": 125, "87": 125, "88": 126, "89": 126, "90": 137, "91": 137, "92": 143, "93": 143, "94": 144, "95": 144, "96": 153, "97": 153, "98": 155, "99": 155, "100": 162, "101": 163, "102": 163, "103": 163, "104": 163, "105": 163, "106": 165, "107": 169, "108": 170, "109": 171, "110": 172, "111": 173, "112": 173, "113": 173, "114": 173, "115": 173, "116": 176, "122": 116}, "filename": "templates/library/import/kodi.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
