# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.3549147
_enable_loop = True
_template_filename = 'templates/library/status.html'
_template_uri = 'templates/library/status.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        head = context.get('head', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        movie_count = context.get('movie_count', UNDEFINED)
        hidden_count = context.get('hidden_count', UNDEFINED)
        profiles = context.get('profiles', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE>\n<html>\n\n<head>\n    ')
        __M_writer(str(head))
        __M_writer('\n    <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/library/status.css?v=002" rel="stylesheet">\n    <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/lib/echo.min.js?v=001" type="text/javascript"></script>\n    <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/status.js?v=005" type="text/javascript"></script>\n    <meta name="movie_count" content="')
        __M_writer(str(movie_count))
        __M_writer('" />\n</head>\n\n<body>\n    ')
        __M_writer(str(navbar))
        __M_writer('\n    <div class="container-fluid clearfix">\n        <div id="toolbar" class="col-md-12">\n            <div id="movie_layout" class="col-md-4 col-sm-6">\n                <div class="btn-group pull-left">\n                    <a class="btn btn-default" data-layout="posters">\n                        <i class="mdi mdi-view-grid"></i>\n                    </a>\n                    <a class="btn btn-default" data-layout="list striped">\n                        <i class="mdi mdi-view-list"></i>\n                    </a>\n                    <a class="btn btn-default" data-layout="compact striped">\n                        <i class="mdi mdi-view-headline"></i>\n                    </a>\n                </div>\n            </div>\n            <div class="col-md-4 col-md-push-4 col-sm-6">\n                <div class="btn-group pull-right">\n                    <select id="movie_sort_key" class="btn btn-default">\n                        <option value="title">')
        __M_writer(str(_('Title')))
        __M_writer('</option>\n                        <option value="year">')
        __M_writer(str(_('Year')))
        __M_writer('</option>\n                        <option value="status">')
        __M_writer(str(_('Status')))
        __M_writer('</option>\n                    </select>\n                    <a class="btn btn-default" id="sort_direction" onclick="switch_sort_direction(event, this)">\n                        <i class="mdi"></i>\n                    </a>\n                </div>\n            </div>\n            <div class="col-md-4 col-md-pull-4 col-sm-12">\n                <span id="page_left" onclick="change_page_sequential(event, -1)">\n                    <i class="mdi mdi-chevron-double-left"></i>\n                    </span>\n                <div class="btn-group">\n                    <select id="page_number" class="btn btn-default">\n                    </select>\n                    <a id="page_count" class="btn btn-default active"></a>\n                </div>\n                <span id="page_right" onclick="change_page_sequential(event, 1)">\n                    <i class="mdi mdi-chevron-double-right"></i>\n                    </span>\n            </div>\n        </div>\n    </div>\n    <div class="container-fluid">\n        <ul id="movie_list" class="hidden striped">\n        </ul>\n        <div id="hidden_count" class="')
        __M_writer(str('hidden' if hidden_count == 0 else ''))
        __M_writer('">\n            <div class="label label-default">\n                ')
        __M_writer(str(hidden_count))
        __M_writer(' Finished movies not shown\n            </div>\n        </div>\n    </div>\n    <div id="overlay"></div>\n    <textarea id="template_movie" class="hidden">\n        <li class="movie" data-imdbid="{imdbid}" onclick="open_info_modal(event, this)">\n            <img data-echo="{url_base}/{poster}" src="{url_base}/static/images/missing_poster.jpg">\n            <span class="label status {status}">{status_translated}</span>\n            <span class="score">\n                <i class="mdi mdi-star-outline"></i>\n                <i class="mdi mdi-star-outline"></i>\n                <i class="mdi mdi-star-outline"></i>\n                <i class="mdi mdi-star-outline"></i>\n                <i class="mdi mdi-star-outline"></i>\n            </span>\n            <span class="title">\n                {title}\n            </span>\n            <span class="year">\n                {year}\n            </span>\n        </li>\n    </textarea>\n    <textarea id="template_movie_info" class="hidden">\n        <div class="modal fade" id="modal_details">\n            <div class="modal-dialog modal-lg">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <h3 class="modal-title">\n                            <span class="title">{title}</span>\n                            <span class="year">{year}</span>\n                        </h3>\n                        <a class="label label-info" href="https://www.themoviedb.org/movie/{tmdbid}" target="_blank" rel="noopener">\n                            TheMovieDB <i class="mdi mdi-earth"></i>\n                        </a>\n                        <a class="label label-info" href="http://www.imdb.com/title/{imdbid}" target="_blank" rel="noopener">\n                            IMDB <i class="mdi mdi-earth"></i>\n                        </a>\n                        <span class="label label-default">\n                            ')
        __M_writer(str(_('Theatrical Release')))
        __M_writer(': {release_date}\n                        </span>\n                        <span class="label label-default">\n                            ')
        __M_writer(str(_('Home Release')))
        __M_writer(': {media_release_date}\n                        </span>\n                        <span class="label label-default">\n                            ')
        __M_writer(str(_('Score')))
        __M_writer(': {score}\n                        </span>\n                        <span class="label label-default">\n                            ')
        __M_writer(str(_('Source')))
        __M_writer(': {origin}\n                        </span>\n                        <span class="label label-default">\n                            ')
        __M_writer(str(_('Date Added')))
        __M_writer(': {added_date}\n                        </span>\n                    </div>\n\n                    <div class="modal-body">\n                        <div class="col-md-3">\n                            <img src="{url_base}/{poster}" class="img-responsive poster">\n                        </div>\n\n                        <div class="col-md-9">\n\n                            <div id="movie_actions" class="col-md-4 btn-group btn-group-justified">\n                                <a class="btn btn-default" title="Force Backlog Search" onclick="manual_search(event, this, \'{imdbid}\')">\n                                    <i class="mdi mdi-magnify"></i>\n                                </a>\n                                <a class="btn btn-default" title="Update Metadata" onclick="update_metadata(event, this, \'{imdbid}\', \'{tmdbid}\')">\n                                    <i class="mdi mdi-tag-text-outline"></i>\n                                </a>\n                                <a class="btn btn-default" title="Remove from Library" onclick="remove_movie(event, this, \'{imdbid}\')">\n                                    <i class="mdi mdi-delete"></i>\n                                </a>\n                            </div>\n\n                            <div id="movie_settings" class="col-md-8">\n                                <div class="col-md-5 col-sm-12">\n                                    <label>')
        __M_writer(str(_('Quality')))
        __M_writer('</label>\n                                    <select id="movie_quality" class="btn btn-default">\n')
        for i in profiles:
            __M_writer('                                        <option value="')
            __M_writer(str(i))
            __M_writer('">')
            __M_writer(str(i))
            __M_writer('</option>\n')
        __M_writer('                                    </select>\n                                </div>\n                                <div class="col-md-5 col-sm-12">\n                                    <label>Status</label>\n                                    <select id="movie_status" class="btn btn-default">\n                                        <option value="Automatic">')
        __M_writer(str(_('Automatic')))
        __M_writer('</option>\n                                        <option value="Disabled">')
        __M_writer(str(_('Finished')))
        __M_writer('</option>\n                                    </select>\n                                </div>\n                                <div class="col-md-2 col-sm-12">\n                                    <a id="update_movie_options" class="btn btn-success" onclick="update_movie_options(event, this, \'{imdbid}\')">\n                                        <i class="mdi mdi-content-save"></i>\n                                    </a>\n                                </div>\n                            </div>\n\n                            <div class="well col-md-12">\n                                <p class="plot">{plot}</p>\n                            </div>\n\n                        </div>\n                        <div id="search_results_table" class="col-md-12 panel panel-default striped">\n                            {table}\n                        </div>\n                    </div>\n\n                    <div class="modal-footer">\n\n                        <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </textarea>\n    <textarea id="template_delete" class="hidden">\n        <div class="modal fade" id="modal_delete">\n            <div class="modal-dialog modal-lg">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <h3 class="modal-title">\n                            ')
        __M_writer(str(_('Remove from Library')))
        __M_writer('\n                        </h3>\n                    </div>\n\n                    <div class="modal-body">\n                        <div class="col-md-12">\n                            ')
        __M_writer(str(_('Are you sure you want to remove <b>{title}</b> from your library?')))
        __M_writer('\n\n                            <div id="delete_file">\n                                <i class="c_box mdi mdi-checkbox-blank-outline" value="False"></i> ')
        __M_writer(str(_('Delete movie file')))
        __M_writer('\n                            </div>\n                        </div>\n\n                    </div>\n\n                    <div class="modal-footer">\n\n                        <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Cancel')))
        __M_writer('</a>\n                        <a class="btn btn-warning pull-right" onclick="_remove_movie(event, this, \'{imdbid}\')">')
        __M_writer(str(_('Remove')))
        __M_writer('</a>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </textarea>\n</body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/library/status.html", "line_map": {"16": 0, "28": 1, "29": 5, "30": 5, "31": 6, "32": 6, "33": 7, "34": 7, "35": 8, "36": 8, "37": 9, "38": 9, "39": 13, "40": 13, "41": 32, "42": 32, "43": 33, "44": 33, "45": 34, "46": 34, "47": 59, "48": 59, "49": 61, "50": 61, "51": 101, "52": 101, "53": 104, "54": 104, "55": 107, "56": 107, "57": 110, "58": 110, "59": 113, "60": 113, "61": 138, "62": 138, "63": 140, "64": 141, "65": 141, "66": 141, "67": 141, "68": 141, "69": 143, "70": 148, "71": 148, "72": 149, "73": 149, "74": 171, "75": 171, "76": 183, "77": 183, "78": 189, "79": 189, "80": 192, "81": 192, "82": 200, "83": 200, "84": 201, "85": 201, "91": 85}, "filename": "templates/library/status.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
