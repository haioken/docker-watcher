# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.449351
_enable_loop = True
_template_filename = 'templates/library/import/plex.html'
_template_uri = 'templates/library/import/plex.html'
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
        __M_writer('/static/css/library/import/plex.css?v=001" rel="stylesheet">\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/import/shared.js?v=001" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/import/plex.js?v=002" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <h1>')
        __M_writer(str(_('Import Plex Library')))
        __M_writer('</h1>\n            <br/>\n            <span id="progress_text"></span>\n            <div class="progress hidden">\n                <div class="progress-bar"></div>\n            </div>\n\n            <div id="csv_upload" class="panel panel-default">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Upload Plex CSV')))
        __M_writer('</h3>\n                    <a href="https://github.com/nosmokingbandit/Watcher3/wiki/Importing-from-other-applications#plex" target="_blank" rel="noopener">\n                        <i class="mdi mdi-help-circle-outline"></i>\n                    </a>\n                </div>\n                <div class="panel-body">\n                    <div class="input-group">\n                        <label class="btn btn-default input-group-btn" for="plex_csv">\n                            <input id="plex_csv" type="file" style="display:none;" onchange="$(\'input#plex_csv_file\').val($(this).val());">\n                            <i class="mdi mdi-file-document"></i>\n                            ')
        __M_writer(str(_('Select CSV')))
        __M_writer('\n                        </label>\n                        <input id="plex_csv_file" class="form-control input-group-item" disabled></input>\n                    </div>\n                </div>\n            </div>\n            <a id="read_csv" class="btn btn-primary" onclick="read_csv(event, this)">\n                <i class="mdi mdi-file-find"></i>\n                ')
        __M_writer(str(_('Read CSV')))
        __M_writer('\n            </a>\n\n            <div id="no_new_movies" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('No New Movies Found')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    ')
        __M_writer(str(_('No new movies have been found in Plex\'s library.')))
        __M_writer('\n                </div>\n            </div>\n\n            <div id="remote_map" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Remote Paths')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <p>')
        __M_writer(str(_('Plex lists file locations relative to itself. If Plex is on a different device than Watcher you may need to alter file paths.')))
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
        __M_writer('\n                        </a>\n                    </div>\n                </div>\n            </div>\n\n            <div id="complete_movies" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Plex Movies')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <table class="table table-hover">\n                        <thead>\n                            <tr>\n                                <th class="shrink">')
        __M_writer(str(_('Import')))
        __M_writer('</th>\n                                <th>')
        __M_writer(str(_('File')))
        __M_writer('</th>\n                                <th>')
        __M_writer(str(_('Title')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('ID')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('Source')))
        __M_writer('</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                        </tbody>\n                    </table>\n                </div>\n            </div>\n\n            <div id="incomplete_movies" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Incomplete Movies')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <p>')
        __M_writer(str(_('The following movies are missing key information. Review and correct as needed.')))
        __M_writer('</p>\n                    <table class="table table-hover">\n                        <thead>\n                            <tr>\n                                <th class="shrink">')
        __M_writer(str(_('Import')))
        __M_writer('</th>\n                                <th class="file_path">')
        __M_writer(str(_('File')))
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
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <table class="table table-hover">\n                        <thead>\n                            <tr>\n                                <th>')
        __M_writer(str(_('Title')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('IMDB ID')))
        __M_writer('</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                        </tbody>\n                    </table>\n                </div>\n            </div>\n\n            <div id="import_error" class="panel panel-danger hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Import Errors')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <table class="table table-hover">\n                        <thead>\n                            <tr>\n                                <th>')
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
{"uri": "templates/library/import/plex.html", "line_map": {"16": 0, "27": 1, "28": 4, "29": 4, "30": 5, "31": 5, "32": 6, "33": 6, "34": 7, "35": 7, "36": 10, "37": 10, "38": 12, "39": 12, "40": 21, "41": 21, "42": 31, "43": 31, "44": 39, "45": 39, "46": 44, "47": 44, "48": 47, "49": 47, "50": 53, "51": 53, "52": 56, "53": 56, "54": 59, "55": 59, "56": 65, "57": 65, "58": 69, "59": 69, "60": 75, "61": 75, "62": 79, "63": 79, "64": 87, "65": 87, "66": 93, "67": 93, "68": 94, "69": 94, "70": 95, "71": 95, "72": 96, "73": 96, "74": 97, "75": 97, "76": 108, "77": 108, "78": 111, "79": 111, "80": 115, "81": 115, "82": 116, "83": 116, "84": 117, "85": 117, "86": 118, "87": 118, "88": 119, "89": 119, "90": 130, "91": 130, "92": 136, "93": 136, "94": 142, "95": 142, "96": 143, "97": 143, "98": 154, "99": 154, "100": 160, "101": 160, "102": 161, "103": 161, "104": 170, "105": 170, "106": 172, "107": 172, "108": 179, "109": 180, "110": 180, "111": 180, "112": 180, "113": 180, "114": 182, "115": 186, "116": 187, "117": 188, "118": 189, "119": 190, "120": 190, "121": 190, "122": 190, "123": 190, "124": 193, "130": 124}, "filename": "templates/library/import/plex.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
