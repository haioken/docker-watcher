# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.3869653
_enable_loop = True
_template_filename = 'templates/library/manage.html'
_template_uri = 'templates/library/manage.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        head = context.get('head', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        movies = context.get('movies', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        profiles = context.get('profiles', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()

        applied_profiles = {i['quality'] for i in movies}
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i','applied_profiles'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/library/manage.css?v=002" rel="stylesheet">\n\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/lib/echo.min.js?v=001" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/library/manage.js?v=003" type="text/javascript"></script>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <div class="well clearfix">\n                <div class="col-md-6">\n                    <div class="btn-group">\n                        <a class="btn btn-default" onclick="select_all()" title="Select All">\n                            <i class="mdi mdi-checkbox-multiple-marked"></i>\n                        </a>\n                        <a class="btn btn-default" onclick="select_none()" title="De-Select All">\n                            <i class="mdi mdi-checkbox-multiple-blank-outline"></i>\n                        </a>\n                        <a class="btn btn-default" onclick="select_inverse()" title="Invert Selection">\n                            <i class="mdi mdi-minus-box"></i>\n                        </a>\n                        <div class="btn-group">\n                            <a class="dropdown-toggle form-control btn btn-default" data-toggle="dropdown" aria-expanded="false">\n                                ')
        __M_writer(str(_('Attribute')))
        __M_writer('\n                            <span class="caret"></span>\n                            </a>\n                            <ul class="dropdown-menu">\n                                <li class="dropdown-cat">')
        __M_writer(str(_('Status')))
        __M_writer('</li>\n                                <li>\n                                    <a data-key="status" data-value="Waiting" onclick="select_attrib(event, this)">')
        __M_writer(str(_('Waiting')))
        __M_writer('</a>\n                                </li>\n                                <li>\n                                    <a data-key="status" data-value="Wanted" onclick="select_attrib(event, this)">')
        __M_writer(str(_('Wanted')))
        __M_writer('</a>\n                                </li>\n                                <li>\n                                    <a data-key="status" data-value="Found" onclick="select_attrib(event, this)">')
        __M_writer(str(_('Found')))
        __M_writer('</a>\n                                </li>\n                                <li>\n                                    <a data-key="status" data-value="Snatched" onclick="select_attrib(event, this)">')
        __M_writer(str(_('Snatched')))
        __M_writer('</a>\n                                </li>\n                                <li>\n                                    <a data-key="status" data-value="Finished" onclick="select_attrib(event, this)">')
        __M_writer(str(_('Finished')))
        __M_writer('</a>\n                                </li>\n                                <li class="divider"></li>\n                                <li class="dropdown-cat">')
        __M_writer(str(_('Quality Profile')))
        __M_writer('</li>\n')
        for i in applied_profiles:
            __M_writer('                                <li>\n                                    <a data-key="quality" data-value="')
            __M_writer(str(i))
            __M_writer('" onclick="select_attrib(event, this)">')
            __M_writer(str(i))
            __M_writer('</a>\n                                </li>\n')
        __M_writer('                            </ul>\n                        </div>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="btn-group pull-right">\n                        <a class="btn btn-success" data-toggle="modal" data-target="#modal_backlog_search">\n                            <i class="mdi mdi-magnify" title="')
        __M_writer(str(_('Force Backlog Search')))
        __M_writer('"></i>\n                        </a>\n                        <a class="btn btn-primary" data-toggle="modal" data-target="#modal_metadata">\n                            <i class="mdi mdi-tag-text-outline" title="')
        __M_writer(str(_('Update Metadata')))
        __M_writer('"></i>\n                        </a>\n                        <a class="btn btn-info" data-toggle="modal" data-target="#modal_quality">\n                            <i class="mdi mdi-video" title="')
        __M_writer(str(_('Change Quality&nbsp;Profile')))
        __M_writer('"></i>\n                        </a>\n                        <a class="btn btn-warning" data-toggle="modal" data-target="#modal_reset">\n                            <i class="mdi mdi-backup-restore" title="')
        __M_writer(str(_('Reset')))
        __M_writer('"></i>\n                        </a>\n                        <a class="btn btn-danger" data-toggle="modal" data-target="#modal_remove">\n                            <i class="mdi mdi-delete" title="')
        __M_writer(str(_('Remove')))
        __M_writer('"></i>\n                        </a>\n                    </div>\n                </div>\n            </div>\n\n            <ul id="movie_list" class="striped">\n')
        for movie in movies:
            __M_writer('                ')
            _status = 'Finished' if movie['status'] == 'Disabled' else movie['status'] 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_status'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\n                ')
            _poster = url_base + '/posters/' + movie['poster'] if movie.get('poster') else url_base + '/static/images/missing_poster.jpg' 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_poster'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\n                 <li class="movie" imdbid="')
            __M_writer(str(movie['imdbid']))
            __M_writer('" data-status="')
            __M_writer(str(_status))
            __M_writer('" data-quality="')
            __M_writer(str(movie['quality']))
            __M_writer('">\n                    <img data-echo="')
            __M_writer(str(_poster))
            __M_writer('" src="')
            __M_writer(str(url_base))
            __M_writer('/static/images/missing_poster.jpg">\n                    <i class="mdi mdi-checkbox-blank-outline c_box" data-imdbid="')
            __M_writer(str(movie['imdbid']))
            __M_writer('" data-tmdbid="')
            __M_writer(str(movie['tmdbid']))
            __M_writer('" value="False"></i>\n                    <span class="label status ')
            __M_writer(str(_status))
            __M_writer('">')
            __M_writer(str(_(_status)))
            __M_writer('</span>\n                    <span class="label label-info quality">')
            __M_writer(str(movie['quality']))
            __M_writer('</span>\n                    <br/>\n                    <span class="title">')
            __M_writer(str(movie['title']))
            __M_writer('</span>\n                    <span class="year">')
            __M_writer(str(movie['year']))
            __M_writer('</span>\n                </li>\n\n')
        __M_writer('            </ul>\n\n\n        </div>\n\n    <!-- Modals for Management Actions -->\n        <div class="modal fade" id="modal_backlog_search">\n            <div class="modal-dialog modal-md">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <h4 class="modal-title">')
        __M_writer(str(_('Backlog Search')))
        __M_writer('</h4>\n                    </div>\n                    <div class="modal-body">\n                        <p>\n                            ')
        __M_writer(str(_('A full backlog search will be performed for selected movies. <br/> Be aware that this will consume one API hit per movie and may take several minutes to complete.')))
        __M_writer('\n                        </p>\n                        <div class="progress hidden">\n                            <div class="progress-bar"></div>\n                        </div>\n                        <table class="table table-striped hidden">\n                            <thead>\n                                <tr>\n                                    <th>IMDB ID</th>\n                                    <th>')
        __M_writer(str(_('Error')))
        __M_writer('</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                            </tbody>\n                        </table>\n                    </div>\n                    <div class="modal-footer">\n                        <div class="btn-group btn-group-justified">\n                            <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                            <a class="btn btn-success" onclick="backlog_search(event, this)">')
        __M_writer(str(_('Force Backlog Search')))
        __M_writer('</a>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n\n        <div class="modal fade" id="modal_metadata">\n            <div class="modal-dialog modal-md">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <h4 class="modal-title">')
        __M_writer(str(_('Update Metadata')))
        __M_writer('</h4>\n                    </div>\n                    <div class="modal-body">\n                        <p>\n                            ')
        __M_writer(str(_('Metadata and posters will be re-downloaded for selected movies. <br/> This may take several minutes.')))
        __M_writer('\n                        </p>\n                        <div class="progress hidden">\n                            <div class="progress-bar"></div>\n                        </div>\n                        <table class="table table-striped hidden">\n                            <thead>\n                                <tr>\n                                    <th>IMDB ID</th>\n                                    <th>')
        __M_writer(str(_('Error')))
        __M_writer('</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                            </tbody>\n                        </table>\n                    </div>\n                    <div class="modal-footer">\n                        <div class="btn-group btn-group-justified">\n                            <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                            <a class="btn btn-primary" onclick="refresh_metadata(event, this)">')
        __M_writer(str(_('Update Metadata')))
        __M_writer('</a>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n\n        <div class="modal fade" id="modal_quality">\n            <div class="modal-dialog modal-md">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <h4 class="modal-title">')
        __M_writer(str(_('Change Quality Profile')))
        __M_writer('</h4>\n                    </div>\n                    <div class="modal-body">\n                        <p>\n                            ')
        __M_writer(str(_('Quality profiles will be changed for selected movies.')))
        __M_writer('\n                            <br/>\n                            <select class="form-control" id="quality" value="">\n                                <option value="" selected="selected" disabled>')
        __M_writer(str(_('Choose a Quality Profile')))
        __M_writer('</option>\n')
        for i in profiles:
            __M_writer('                                <option value="')
            __M_writer(str(i))
            __M_writer('">')
            __M_writer(str(i))
            __M_writer('</option>\n')
        __M_writer('                        </select>\n                        </p>\n                        <div class="progress hidden">\n                            <div class="progress-bar"></div>\n                        </div>\n                        <table class="table table-striped hidden">\n                            <thead>\n                                <tr>\n                                    <th>IMDB ID</th>\n                                    <th>')
        __M_writer(str(_('Error')))
        __M_writer('</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                            </tbody>\n                        </table>\n                    </div>\n                    <div class="modal-footer">\n                        <div class="btn-group btn-group-justified">\n                            <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                            <a class="btn btn-info" onclick="change_quality(event, this)">')
        __M_writer(str(_('Change Quality Profile')))
        __M_writer('</a>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n\n        <div class="modal fade" id="modal_reset">\n            <div class="modal-dialog modal-md">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <h4 class="modal-title">')
        __M_writer(str(_('Reset Movies')))
        __M_writer('</h4>\n                    </div>\n                    <div class="modal-body">\n                        <p>\n                            ')
        __M_writer(str(_('Selected movies will be reset.<br/>Quality Profile will be set to Default.<br/>Status will be set to wanted.<br/>Search Results will be removed (including Imports).<br/>This cannot be undone.')))
        __M_writer('\n                        </p>\n                        <div class="progress hidden">\n                            <div class="progress-bar"></div>\n                        </div>\n                        <table class="table table-striped hidden">\n                            <thead>\n                                <tr>\n                                    <th>IMDB ID</th>\n                                    <th>')
        __M_writer(str(_('Error')))
        __M_writer('</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                            </tbody>\n                        </table>\n                    </div>\n\n                    <div class="modal-footer">\n                        <div class="btn-group btn-group-justified">\n                            <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                            <a class="btn btn-warning" onclick="reset_movies(event, this)">')
        __M_writer(str(_('Reset Movies')))
        __M_writer('</a>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n\n        <div class="modal fade" id="modal_remove">\n            <div class="modal-dialog modal-md">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <h4 class="modal-title">')
        __M_writer(str(_('Remove Movies')))
        __M_writer('</h4>\n                    </div>\n                    <div class="modal-body">\n                        <p>\n                            ')
        __M_writer(str(_('Selected movies will be removed from the library.<br/>This will not delete movie files.<br/>This cannot be undone.')))
        __M_writer('\n                        </p>\n                        <div class="progress hidden">\n                            <div class="progress-bar"></div>\n                        </div>\n                        <table class="table table-striped hidden">\n                            <thead>\n                                <tr>\n                                    <th>IMDB ID</th>\n                                    <th>')
        __M_writer(str(_('Error')))
        __M_writer('</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                            </tbody>\n                        </table>\n                    </div>\n                    <div class="modal-footer">\n                        <div class="btn-group btn-group-justified">\n                            <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                            <a class="btn btn-danger" onclick="remove_movies(event, this)">')
        __M_writer(str(_('Remove Movies')))
        __M_writer('</a>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/library/manage.html", "line_map": {"16": 0, "27": 1, "33": 3, "34": 8, "35": 8, "36": 9, "37": 9, "38": 11, "39": 11, "40": 12, "41": 12, "42": 14, "43": 14, "44": 30, "45": 30, "46": 34, "47": 34, "48": 36, "49": 36, "50": 39, "51": 39, "52": 42, "53": 42, "54": 45, "55": 45, "56": 48, "57": 48, "58": 51, "59": 51, "60": 52, "61": 53, "62": 54, "63": 54, "64": 54, "65": 54, "66": 57, "67": 64, "68": 64, "69": 67, "70": 67, "71": 70, "72": 70, "73": 73, "74": 73, "75": 76, "76": 76, "77": 83, "78": 84, "79": 84, "83": 84, "84": 85, "88": 85, "89": 86, "90": 86, "91": 86, "92": 86, "93": 86, "94": 86, "95": 87, "96": 87, "97": 87, "98": 87, "99": 88, "100": 88, "101": 88, "102": 88, "103": 89, "104": 89, "105": 89, "106": 89, "107": 90, "108": 90, "109": 92, "110": 92, "111": 93, "112": 93, "113": 97, "114": 107, "115": 107, "116": 111, "117": 111, "118": 120, "119": 120, "120": 129, "121": 129, "122": 130, "123": 130, "124": 141, "125": 141, "126": 145, "127": 145, "128": 154, "129": 154, "130": 163, "131": 163, "132": 164, "133": 164, "134": 175, "135": 175, "136": 179, "137": 179, "138": 182, "139": 182, "140": 183, "141": 184, "142": 184, "143": 184, "144": 184, "145": 184, "146": 186, "147": 195, "148": 195, "149": 204, "150": 204, "151": 205, "152": 205, "153": 216, "154": 216, "155": 220, "156": 220, "157": 229, "158": 229, "159": 239, "160": 239, "161": 240, "162": 240, "163": 251, "164": 251, "165": 255, "166": 255, "167": 264, "168": 264, "169": 273, "170": 273, "171": 274, "172": 274, "178": 172}, "filename": "templates/library/manage.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
