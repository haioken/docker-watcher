# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.4846268
_enable_loop = True
_template_filename = 'templates/add_movie.html'
_template_uri = 'templates/add_movie.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        head = context.get('head', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        len = context.get('len', UNDEFINED)
        profiles = context.get('profiles', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/add_movie.css?v=001" rel="stylesheet">\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/add_movie.js?v=001" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n\n            <div class="input-group" id="search_bar">\n                <input type="text" id="apikey" class="form-control">\n                <span class="input-group-btn">\n                    <a id="search_button" class="btn btn-default" onclick="search_tmdb(event, this)">\n                        <i class="mdi mdi-magnify"></i>\n                    </a>\n                </span>\n            </div>\n\n            <ul id="movies">\n\n            </ul>\n        </div>\n\n        <textarea id="movie_template" class="hidden">\n            <li class="movie">\n                <img src="{img_url}">\n                <div class="movie_actions btn-group btn-group-justified">\n                    <div class="btn-group">\n                        <span type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">\n                            ')
        __M_writer(str(_('Add')))
        __M_writer('\n                            <i class="mdi mdi-chevron-down"></i>\n                        </span>\n                        <ul class="dropdown-menu dropdown-menu-left dropdown-menu-wide">\n                            <li>\n                                <a onclick="add_movie(event, this, \'Default\')">\n                                    ')
        __M_writer(str(_('Default')))
        __M_writer('\n                                </a>\n                            </li>\n')
        if len(profiles) > 0:
            __M_writer('                            <li class="divider"></li>\n')
        for profile in profiles:
            __M_writer('                            <li>\n                                <a onclick="add_movie(event, this, \'')
            __M_writer(str(profile))
            __M_writer('\')">\n                                    ')
            __M_writer(str(profile))
            __M_writer('\n                                </a>\n                            </li>\n')
        __M_writer('                        </ul>\n                    </div>\n\n                    <div class="btn-group">\n                        <a class="btn btn-default" onclick="show_details(event, this)">')
        __M_writer(str(_('Details')))
        __M_writer('</a>\n                    </div>\n                </div>\n                <span class="title">{title}</span>\n                <span class="year">{year}</span>\n            </li>\n        </textarea>\n        <textarea id="details_template" class="hidden">\n            <div class="modal fade" id="modal_details">\n                <div class="modal-dialog modal-lg">\n                    <div class="modal-content">\n                        <div class="modal-header">\n                            <h3 class="modal-title">\n                                {title}\n                                <span class="year">{year}</span>\n                            </h3>\n                            <span class="label label-default">\n                                ')
        __M_writer(str(_('Theatrical Release')))
        __M_writer(': {release_date}\n                            </span>\n                            <span class="label label-default">\n                                ')
        __M_writer(str(_('Score')))
        __M_writer(': {vote_average}\n                            </span>\n                            <a class="label label-info" href="https://www.themoviedb.org/movie/{id}" target="_blank" rel="noopener">\n                                TheMovieDB <i class="mdi mdi-earth"></i>\n                            </a>\n                        </div>\n\n                        <div class="modal-body">\n\n                            <div class="col-md-5">\n                                <img src="{poster_url}" class="img-responsive">\n                            </div>\n                            <div class="col-md-7">\n                                <div class="embed-responsive embed-responsive-16by9">\n                                    <iframe src="" id="trailer"></iframe>\n                                </div>\n                            </div>\n                            <div class="col-md-7">\n                                <div class="well">\n                                    <p class="plot">{overview}</p>\n                                </div>\n                            </div>\n                        </div>\n\n                        <div class="modal-footer">\n                            <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                            <div class="btn-group pull-right">\n                                <span type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">\n                                    ')
        __M_writer(str(_('Add')))
        __M_writer('\n                                    <i class="mdi mdi-chevron-down"></i>\n                                </span>\n                                <ul class="dropdown-menu dropdown-menu-left dropdown-menu-wide">\n                                    <li>\n                                        <a onclick="add_movie(event, this, \'Default\', modal=true)">\n                                            ')
        __M_writer(str(_('Default')))
        __M_writer('\n                                        </a>\n                                    </li>\n')
        if len(profiles) > 0:
            __M_writer('                                    <li class="divider"></li>\n')
        for profile in profiles:
            __M_writer('                                    <li>\n                                        <a onclick="add_movie(event, this, \'')
            __M_writer(str(profile))
            __M_writer('\', modal=true)">\n                                            ')
            __M_writer(str(profile))
            __M_writer('\n                                        </a>\n                                    </li>\n')
        __M_writer('                                </ul>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </textarea>\n\n        <div id="thinker">\n            <i class="mdi mdi-circle-outline animated"></i>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/add_movie.html", "line_map": {"16": 0, "27": 1, "28": 4, "29": 4, "30": 5, "31": 5, "32": 6, "33": 6, "34": 9, "35": 9, "36": 32, "37": 32, "38": 38, "39": 38, "40": 41, "41": 42, "42": 44, "43": 45, "44": 46, "45": 46, "46": 47, "47": 47, "48": 51, "49": 55, "50": 55, "51": 72, "52": 72, "53": 75, "54": 75, "55": 100, "56": 100, "57": 103, "58": 103, "59": 109, "60": 109, "61": 112, "62": 113, "63": 115, "64": 116, "65": 117, "66": 117, "67": 118, "68": 118, "69": 122, "75": 69}, "filename": "templates/add_movie.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
