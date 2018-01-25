# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.468674
_enable_loop = True
_template_filename = 'templates/library/import/directory.html'
_template_uri = 'templates/library/import/directory.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        head = context.get('head', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        file_list = context.get('file_list', UNDEFINED)
        profiles = context.get('profiles', UNDEFINED)
        current_dir = context.get('current_dir', UNDEFINED)
        sources = context.get('sources', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/library/import/directory.css?v=001" rel="stylesheet">\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/import/shared.js?v=001" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/import/directory.js?v=001" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <h1>')
        __M_writer(str(_('Import Directory')))
        __M_writer('</h1>\n            <br/>\n            <span id="progress_text"></span>\n            <div class="progress hidden">\n                <div class="progress-bar"></div>\n            </div>\n\n            <div id="select_directory" class="panel panel-default">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Select Directory')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <div class="col-md-12">\n                        <div class="input-group">\n                            <span class="input-group-item">\n                                <input type="text" id="directory_input" class="form-control">\n                            </span>\n                            <span class="input-group-btn">\n                                <a class="btn btn-default" data-toggle="modal" data-target="#modal_browser">\n                                    <i class="mdi mdi-folder-open"></i>\n                                </a>\n                            </span>\n                        </div>\n                    </div>\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('Minimum File Size')))
        __M_writer('</label>\n                        <div class="input-group">\n                            <span class="input-group-item">\n                                <input type="number" id="min_file_size" class="form-control" min="0" value="500">\n                            </span>\n                            <span class="input-group-addon">\n                                ')
        __M_writer(str(_('MegaBytes')))
        __M_writer('\n                            </span>\n                        </div>\n                    </div>\n                    <div class="col-md-6">\n                        <label>')
        __M_writer(str(_('Scan Recursively')))
        __M_writer('</label>\n                        <div class="input-group">\n                            <span class="input-group-addon">\n                                <i id="scan_recursive" class="mdi mdi-checkbox-marked c_box" value="True"></i>\n                            </span>\n                            <span class="input-group-item form-control">\n                                ')
        __M_writer(str(_('Scan sub-folders as well.')))
        __M_writer('\n                            </span>\n                        </div>\n                    </div>\n                </div>\n            </div>\n            <a id="scan_dir" class="btn btn-primary" onclick="scan_library(event, this)">\n                <i class="mdi mdi-file-find"></i>\n                ')
        __M_writer(str(_('Scan Directory')))
        __M_writer('\n            </a>\n\n            <div id="no_new_movies" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('No New Movies Found')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    ')
        __M_writer(str(_('No new movies have been found.')))
        __M_writer('\n                </div>\n            </div>\n\n            <div id="complete_movies" class="panel panel-default hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Found Movies')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <table class="table table-hover">\n                        <thead>\n                            <tr>\n                                <th class="shrink">')
        __M_writer(str(_('Import')))
        __M_writer('</th>\n                                <th>')
        __M_writer(str(_('File')))
        __M_writer('</th>\n                                <th>')
        __M_writer(str(_('Title')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('TheMovieDB&nbsp;ID')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('Source')))
        __M_writer('</th>\n                                <th>')
        __M_writer(str(_('Size')))
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
        __M_writer(str(_('TheMovieDB&nbsp;ID')))
        __M_writer('</th>\n                                <th class="shrink">')
        __M_writer(str(_('Source')))
        __M_writer('</th>\n                                <th>')
        __M_writer(str(_('Size')))
        __M_writer('</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                        </tbody>\n                    </table>\n                </div>\n            </div>\n\n            <a id="import_library" class="btn btn-primary hidden" onclick="import_library(event, this)">\n                <i class="mdi mdi-archive"></i>\n                ')
        __M_writer(str(_('Import Library')))
        __M_writer('\n            </a>\n\n            <div id="import_success" class="panel panel-success hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(_('Imported Movies')))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n                    <table class="table table-hover">\n                        <thead>\n                            <tr>\n                                <th>')
        __M_writer(str(_('Title')))
        __M_writer('</th>\n                                <th class="shrink">\n                                    ')
        __M_writer(str(_('TheMovieDB&nbsp;ID')))
        __M_writer('\n                                    <a href="https://www.themoviedb.org/">\n                                        <i class="mdi mdi-globe"></i>\n                                    </a>\n                                </th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                        </tbody>\n                    </table>\n                </div>\n            </div>\n\n            <div id="import_error" class="panel panel-danger hidden">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
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
        __M_writer('            </select>\n        </textarea>\n\n        <div id="modal_browser" class="modal fade">\n            <div class="modal-dialog">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <h4 class="modal-title">')
        __M_writer(str(_('Select Library Directory')))
        __M_writer('</h4>\n                    </div>\n                    <div class="modal-body">\n                        <div class="well col-md-12" id="modal_current_dir">\n                            ')
        __M_writer(str(current_dir))
        __M_writer('\n                        </div>\n\n                        <ul id="modal_file_list" class="list-group">\n')
        for i in file_list:
            __M_writer('                            <li class="col-md-6 list-group-item">\n                                <i class="mdi mdi-folder"></i>\n                                ')
            __M_writer(str(i))
            __M_writer('\n                            </li>\n')
        __M_writer('                        </ul>\n                    </div>\n                    <div class="modal-footer">\n                        <a type="button" class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                        <a type="button" class="btn btn-primary pull-right" onclick="file_browser_select(event, this)">')
        __M_writer(str(_('Select')))
        __M_writer('</a>\n                    </div>\n                </div>\n            </div>\n        </div>\n\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/library/import/directory.html", "line_map": {"16": 0, "29": 1, "30": 4, "31": 4, "32": 5, "33": 5, "34": 6, "35": 6, "36": 7, "37": 7, "38": 10, "39": 10, "40": 12, "41": 12, "42": 21, "43": 21, "44": 37, "45": 37, "46": 43, "47": 43, "48": 48, "49": 48, "50": 54, "51": 54, "52": 62, "53": 62, "54": 67, "55": 67, "56": 70, "57": 70, "58": 76, "59": 76, "60": 82, "61": 82, "62": 83, "63": 83, "64": 84, "65": 84, "66": 85, "67": 85, "68": 86, "69": 86, "70": 87, "71": 87, "72": 98, "73": 98, "74": 101, "75": 101, "76": 105, "77": 105, "78": 106, "79": 106, "80": 107, "81": 107, "82": 108, "83": 108, "84": 109, "85": 109, "86": 110, "87": 110, "88": 121, "89": 121, "90": 126, "91": 126, "92": 132, "93": 132, "94": 134, "95": 134, "96": 149, "97": 149, "98": 155, "99": 155, "100": 156, "101": 156, "102": 165, "103": 165, "104": 167, "105": 167, "106": 174, "107": 175, "108": 175, "109": 175, "110": 175, "111": 175, "112": 177, "113": 181, "114": 182, "115": 183, "116": 184, "117": 185, "118": 185, "119": 185, "120": 185, "121": 185, "122": 188, "123": 195, "124": 195, "125": 199, "126": 199, "127": 203, "128": 204, "129": 206, "130": 206, "131": 209, "132": 212, "133": 212, "134": 213, "135": 213, "141": 135}, "filename": "templates/library/import/directory.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
