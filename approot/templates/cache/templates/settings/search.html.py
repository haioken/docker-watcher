# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.5531042
_enable_loop = True
_template_filename = 'templates/settings/search.html'
_template_uri = 'templates/settings/search.html'
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
        config = context.get('config', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/shared.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/search.css?v=001" rel="stylesheet">\n\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/shared.js?v=002" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/search.js?v=001" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n\n            <h1>')
        __M_writer(str(_('Search')))
        __M_writer('</h1>\n\n            <form class="form-horizontal well" data-category="search">\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Search Immediately')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="searchafteradd" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['searchafteradd']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Search immediately after adding movie')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Grab Best Release')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="autograb" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['autograb']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Automatically grab best release')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Verify Availability')))
        __M_writer('</label>\n                    <select id="verifyreleases" class="form-control select-sm" value="')
        __M_writer(str(config['verifyreleases']))
        __M_writer('">\n                        <option value="">')
        __M_writer(str(_('Disabled')))
        __M_writer('</option>\n                        <option value="predb">PreDB</option>\n                        <option value="mediareleasedate">')
        __M_writer(str(_('Home Media Release Date')))
        __M_writer('</option>\n                    </select>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Skip verification if Movie is older than [X] weeks')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="verifyreleasesskip" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['verifyreleasesskip']))
        __M_writer('"></i>\n                        </span>\n                        <input type="number" id="verifyreleasesskipweeks" class="form-control" min="0" placeholder="26" value="')
        __M_writer(str(config['verifyreleasesskipweeks']))
        __M_writer('">\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Sync RSS Every [X] Minutes')))
        __M_writer('</label>\n                    <input type="number" id="rsssyncfrequency" class="form-control" min="15" placeholder="120" value="')
        __M_writer(str(config['rsssyncfrequency']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-12 separator"></div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Wait [X] Days To Grab')))
        __M_writer('</label>\n                    <input type="number" id="waitdays" class="form-control" min="0" placeholder="3" value="')
        __M_writer(str(config['waitdays']))
        __M_writer('">\n                </div>\n\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Skip Wait if Movie is Older than [X] Weeks')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="skipwait" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['skipwait']))
        __M_writer('"></i>\n                        </span>\n                        <input type="number" id="skipwaitweeks" class="form-control" min="0" placeholder="26" value="')
        __M_writer(str(config['skipwaitweeks']))
        __M_writer('">\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Keep Searching [X] Days for Best Release')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="keepsearching" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['keepsearching']))
        __M_writer('"></i>\n                        </span>\n                        <input type="number" id="keepsearchingdays" class="form-control" min="0" placeholder="7" value="')
        __M_writer(str(config['keepsearchingdays']))
        __M_writer('">\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Re-Grabbed Releases Must Score [X] Points Higher')))
        __M_writer('</label>\n                    <input type="number" id="keepsearchingscore" class="form-control" min="0" placeholder="10" value="')
        __M_writer(str(config['keepsearchingscore']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-12 separator"></div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Torrents Must Have [X] Seeds')))
        __M_writer('</label>\n                    <input type="number" id="mintorrentseeds" class="form-control" min="0" placeholder="1" value="')
        __M_writer(str(config['mintorrentseeds']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Add [X] Points to Freeleech Torrents')))
        __M_writer('</label>\n                    <input type="number" id="freeleechpoints" class="form-control" min="0" placeholder="10" value="')
        __M_writer(str(config['freeleechpoints']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Usenet Server Retention')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <input type="number" id="retention" class="form-control" min="0" placeholder="1500" value="')
        __M_writer(str(config['retention']))
        __M_writer('">\n                        <span class="input-group-addon">\n                            ')
        __M_writer(str(_('Days')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n            </form>\n\n            <h1>')
        __M_writer(str(_('Watchlists')))
        __M_writer('</h1>\n\n            <form class="form-horizontal well" data-category="watchlists">\n                * (12.19.17) IMDB has disabled RSS lists and may not sync\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Sync IMDB Watchlists Every [X] Minutes')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="imdbsync" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Watchlists']['imdbsync']))
        __M_writer('"></i>\n                        </span>\n                        <input type="number" id="imdbfrequency" class="form-control" min="15" placeholder="60" value="')
        __M_writer(str(config['Watchlists']['imdbfrequency']))
        __M_writer('">\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('IMDB Watchlist URLs')))
        __M_writer('</label>\n                    <input type="text" id="imdbrss" class="form-control" placeholder="http://rss.imdb.com/user/..." value="')
        __M_writer(str(', '.join(config['Watchlists']['imdbrss'])))
        __M_writer('" data-toggle="tooltip" title="')
        __M_writer(str(_('Separate lists with commas')))
        __M_writer('">\n                </div>\n\n                <div class="col-md-12 separator"></div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Sync Popular Movies Every Day At')))
        __M_writer('\n                        <a href="https://github.com/sjlu/popular-movies" target="_blank" rel="noopener">\n                            &nbsp;<i class="mdi mdi-help-circle-outline"></i>\n                        </a>\n                    </label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="popularmoviessync" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Watchlists']['popularmoviessync']))
        __M_writer('"></i>\n                        </span>\n                        <input type="time" id="popularmoviestime" class="form-control" data-hour="')
        __M_writer(str(config['Watchlists']['popularmovieshour']))
        __M_writer('" data-minute="')
        __M_writer(str(config['Watchlists']['popularmoviesmin']))
        __M_writer('" value="">\n                    </div>\n                </div>\n\n                <div class="col-md-12 separator"></div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Sync Trakt Lists Every [X] Minutes')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="traktsync" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Watchlists']['traktsync']))
        __M_writer('"></i>\n                        </span>\n                        <input type="number" id="traktfrequency" class="form-control" min="15" placeholder="60" value="')
        __M_writer(str(config['Watchlists']['traktfrequency']))
        __M_writer('">\n                    </div>\n                </div>\n\n                <div class="col-md-3">\n                    <label>')
        __M_writer(str(_('Max Movies Per List')))
        __M_writer('</label>\n                    <input type="number" id="traktlength" class="form-control" min="1" placeholder="10" value="')
        __M_writer(str(config['Watchlists']['traktlength']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-3">\n                    <label>')
        __M_writer(str(_('Minimum Score')))
        __M_writer('</label>\n                    <input type="number" id="traktscore" class="form-control" min="0" placeholder="7" value="')
        __M_writer(str(config['Watchlists']['traktscore']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Trakt Watchlist URLs')))
        __M_writer('</label>\n                    <input type="text" id="traktrss" class="form-control" placeholder="https://trakt.tv/users/user/lists/movielist.atom?..." value="')
        __M_writer(str(config['Watchlists']['traktrss']))
        __M_writer('" data-toggle="tooltip" title="')
        __M_writer(str(_('Separate lists with commas')))
        __M_writer('">\n                </div>\n\n                <div class="col-md-12"></div>\n\n                <div class="col-md-3">\n                    <label>')
        __M_writer(str(_('Trakt Lists')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="collected" class="mdi mdi-checkbox-blank-outline c_box" data-sub-category="traktlist" value="')
        __M_writer(str(config['Watchlists']['Traktlists']['collected']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Collected')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-3">\n                    <label>&nbsp;</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="popular" class="mdi mdi-checkbox-blank-outline c_box" data-sub-category="traktlist" value="')
        __M_writer(str(config['Watchlists']['Traktlists']['popular']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Popular')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-3">\n                    <label>&nbsp;</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="anticipated" class="mdi mdi-checkbox-blank-outline c_box" data-sub-category="traktlist" value="')
        __M_writer(str(config['Watchlists']['Traktlists']['anticipated']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Anticipated')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-3">\n                    <label>&nbsp;</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="trending" class="mdi mdi-checkbox-blank-outline c_box" data-sub-category="traktlist" value="')
        __M_writer(str(config['Watchlists']['Traktlists']['trending']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Trending')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-3">\n                    <label></label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="boxoffice" class="mdi mdi-checkbox-blank-outline c_box" data-sub-category="traktlist" value="')
        __M_writer(str(config['Watchlists']['Traktlists']['boxoffice']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Boxoffice')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-3">\n                    <label></label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="watched" class="mdi mdi-checkbox-blank-outline c_box" data-sub-category="traktlist" value="')
        __M_writer(str(config['Watchlists']['Traktlists']['watched']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Watched')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n            </form>\n\n            <a id="save_settings" class="btn btn-success pull-right" onclick="save_settings(event, this)">\n                <i class="mdi mdi-content-save"></i>\n                ')
        __M_writer(str(_('Save Settings')))
        __M_writer('\n            </a>\n\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/settings/search.html", "line_map": {"16": 0, "26": 1, "27": 4, "28": 4, "29": 5, "30": 5, "31": 6, "32": 6, "33": 8, "34": 8, "35": 9, "36": 9, "37": 12, "38": 12, "39": 15, "40": 15, "41": 20, "42": 20, "43": 23, "44": 23, "45": 26, "46": 26, "47": 32, "48": 32, "49": 35, "50": 35, "51": 38, "52": 38, "53": 44, "54": 44, "55": 45, "56": 45, "57": 46, "58": 46, "59": 48, "60": 48, "61": 53, "62": 53, "63": 56, "64": 56, "65": 58, "66": 58, "67": 63, "68": 63, "69": 64, "70": 64, "71": 70, "72": 70, "73": 71, "74": 71, "75": 76, "76": 76, "77": 79, "78": 79, "79": 81, "80": 81, "81": 86, "82": 86, "83": 89, "84": 89, "85": 91, "86": 91, "87": 96, "88": 96, "89": 97, "90": 97, "91": 103, "92": 103, "93": 104, "94": 104, "95": 108, "96": 108, "97": 109, "98": 109, "99": 113, "100": 113, "101": 115, "102": 115, "103": 117, "104": 117, "105": 123, "106": 123, "107": 128, "108": 128, "109": 131, "110": 131, "111": 133, "112": 133, "113": 138, "114": 138, "115": 139, "116": 139, "117": 139, "118": 139, "119": 145, "120": 145, "121": 152, "122": 152, "123": 154, "124": 154, "125": 154, "126": 154, "127": 161, "128": 161, "129": 164, "130": 164, "131": 166, "132": 166, "133": 171, "134": 171, "135": 172, "136": 172, "137": 176, "138": 176, "139": 177, "140": 177, "141": 181, "142": 181, "143": 182, "144": 182, "145": 182, "146": 182, "147": 188, "148": 188, "149": 191, "150": 191, "151": 194, "152": 194, "153": 202, "154": 202, "155": 205, "156": 205, "157": 213, "158": 213, "159": 216, "160": 216, "161": 224, "162": 224, "163": 227, "164": 227, "165": 235, "166": 235, "167": 238, "168": 238, "169": 246, "170": 246, "171": 249, "172": 249, "173": 257, "174": 257, "180": 174}, "filename": "templates/settings/search.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
