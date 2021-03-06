# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.725862
_enable_loop = True
_template_filename = 'templates/settings/postprocessing.html'
_template_uri = 'templates/settings/postprocessing.html'
_source_encoding = 'ascii'
_exports = ['render_remote_map']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        head = context.get('head', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        config = context.get('config', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        def render_remote_map(remote,local):
            return render_render_remote_map(context._locals(__M_locals),remote,local)
        os = context.get('os', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')

        tags = '{title} {sort_title} {year} {resolution} {rated} {edition} {imdbid} {videocodec} {audiocodec} {releasegroup} {source} {quality}'
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tags'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/shared.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/postprocessing.css?v=001" rel="stylesheet">\n\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/shared.js?v=002" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/postprocessing.js?v=001" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n\n            <h1>')
        __M_writer(str(_('Postprocessing')))
        __M_writer('</h1>\n\n            <div class="col-md-12 well">\n                ')
        __M_writer(str(_('See the Wiki for help configuring your download client.')))
        __M_writer('\n                <a href="https://github.com/nosmokingbandit/watcher3/wiki", target="_blank" rel="noopener">\n                    <i class="mdi mdi-help-circle-outline"></i>\n                </a>\n            </div>\n\n            <form class="form-horizontal well" data-category="postprocessing">\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Delete Failed Downloads')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="cleanupfailed" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['cleanupfailed']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Delete incomplete or failed downloads')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-12 separator"></div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Rename Movies')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="renamerenabled" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['renamerenabled']))
        __M_writer('"></i>\n                        </span>\n                        <input type="text" id="renamerstring" class="form-control" placeholder="{title} ({year})" value="')
        __M_writer(str(config['renamerstring']))
        __M_writer('" data-toggle="tooltip" title="')
        __M_writer(str(tags))
        __M_writer('">\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Use Periods For Spaces')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="replacespaces" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['replacespaces']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Replace all spaces with periods')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-12 separator"></div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Move Movies')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="moverenabled" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['moverenabled']))
        __M_writer('"></i>\n                        </span>\n                        <input type="text" id="moverpath" class="form-control" placeholder="/users/ricksanchez/movies/{title} ({year})/" value="')
        __M_writer(str(config['moverpath']))
        __M_writer('" data-toggle="tooltip" title="')
        __M_writer(str(tags))
        __M_writer('">\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Move Method')))
        __M_writer('</label>\n                    <select class="form-control select-sm" id="movermethod" value="')
        __M_writer(str(config['movermethod']))
        __M_writer('">\n                        <option value="move">')
        __M_writer(str(_('Move')))
        __M_writer('</option>\n                        <option value="copy">')
        __M_writer(str(_('Copy')))
        __M_writer('</option>\n                        <option value="hardlink">')
        __M_writer(str(_('Hardlink')))
        __M_writer('</option>\n                        <option value="symboliclink" ')
        __M_writer(str('disabled=true' if os == 'windows' else ''))
        __M_writer('>')
        __M_writer(str(_('Symbolic Link')))
        __M_writer('</option>\n                    </select>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Move Additional File Types')))
        __M_writer('</label>\n                    <input type="text" id="moveextensions" class="form-control" placeholder="srt, nfo" value="')
        __M_writer(str(config['moveextensions']))
        __M_writer('" data-toggle="tooltip" title="')
        __M_writer(str(_('Separate file extensions with commas')))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Clean Up Download Dir')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="cleanupenabled" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['cleanupenabled']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Remove leftover files after move')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Replace Illegal Characters With [X]')))
        __M_writer('</label>\n                    <input type="text" id="replaceillegal" class="form-control" value="')
        __M_writer(str(config['replaceillegal']))
        __M_writer('" data-toggle="tooltip" title="')
        __M_writer(str(_('Cannot contain *&nbsp;?&nbsp;&quot;&nbsp;;&nbsp;&lt;&nbsp;&gt;&nbsp;|')))
        __M_writer('\'">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Clean Up Target Dir')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="removeadditionalfiles" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['removeadditionalfiles']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Remove associated files before moving.')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-12 separator"></div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Use Recycle Bin Folder')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="recyclebinenabled" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['recyclebinenabled']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Keep old movies when re-downloading.')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Recycle Bin Directory')))
        __M_writer('</label>\n                    <input type="text" id="recyclebindirectory" class="form-control" value="')
        __M_writer(str(config['recyclebindirectory']))
        __M_writer('">\n                </div>\n\n            </form>\n\n            <h1>')
        __M_writer(str(_('Directory Scanner')))
        __M_writer('</h1>\n            <form class="form-horizontal well" data-category="scanner">\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Enable Scanner')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="enabled" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Scanner']['enabled']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Scan directory for movies to process.')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Scan Directory')))
        __M_writer('</label>\n                    <input type="text" id="directory" class="form-control" value="')
        __M_writer(str(config['Scanner']['directory']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Scan Frequency')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <input type="number" id="interval" class="form-control" min="5" placeholder="240" value="')
        __M_writer(str(config['Scanner']['interval']))
        __M_writer('">\n                        <span class="input-group-addon">\n                            ')
        __M_writer(str(_('Minutes')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Only Process New Files')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="newfilesonly" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Scanner']['newfilesonly']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Only process files added since last scan.')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Minimum File Size')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <input type="number" id="minsize" class="form-control" min="0" placeholder="500" value="')
        __M_writer(str(config['Scanner']['minsize']))
        __M_writer('">\n                        <span class="input-group-addon">\n                            ')
        __M_writer(str(_('MB')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n            </form>\n\n            <h1>')
        __M_writer(str(_('Remote Mapping')))
        __M_writer('</h1>\n            <a href="https://github.com/nosmokingbandit/Watcher3/wiki/Remote-Mapping" target="_blank" rel="noopener">\n                <i class="mdi mdi-help-circle-outline"></i>\n            </a>\n            <form class="form-horizontal well" data-category="remote_mapping">\n                <table class="table table-hover">\n                    <thead>\n                        <th>')
        __M_writer(str(_('Remote Path')))
        __M_writer('</th>\n                        <th>')
        __M_writer(str(_('Local Path')))
        __M_writer('</th>\n                        <th></th>\n                    </thead>\n                    <tbody>\n')
        for remote, local in config['RemoteMapping'].items():
            __M_writer('                        ')
            __M_writer(str(render_remote_map(remote, local)))
            __M_writer('\n')
        __M_writer('                    </tbody>\n                </table>\n                <div class=\'col-md-12\'>\n                    <a class="btn btn-primary" onclick="add_mapping(event, this)">\n                        <i class="mdi mdi-plus"></i>\n                        ')
        __M_writer(str(_('Add Mapping')))
        __M_writer('\n                    </a>\n                </div>\n            </form>\n\n            <a id="save_settings" class="btn btn-success pull-right" onclick="save_settings(event, this)">\n                <i class="mdi mdi-content-save"></i>\n                ')
        __M_writer(str(_('Save Settings')))
        __M_writer('\n            </a>\n        </div>\n        <textarea id="template_mapping" class="hidden">\n            ')
        __M_writer(str(render_remote_map('', '')))
        __M_writer('\n        </textarea>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_remote_map(context,remote,local):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    <tr>\n        <td>\n            <input type="text" data-id="remote" class="form-control" placeholder="/users/rick_sanchez/movies" value="')
        __M_writer(str(remote))
        __M_writer('">\n        </td>\n        <td>\n            <input type="text" data-id="local" class="form-control" placeholder="//server/downloads/movies" value="')
        __M_writer(str(local))
        __M_writer('">\n        </td>\n        <td>\n            <a class="btn btn-danger" onclick="remove_mapping(event, this)">\n                <i class="mdi mdi-delete"></i>\n            </a>\n        </td>\n    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/settings/postprocessing.html", "line_map": {"16": 0, "29": 15, "30": 17, "36": 19, "37": 24, "38": 24, "39": 25, "40": 25, "41": 26, "42": 26, "43": 28, "44": 28, "45": 29, "46": 29, "47": 32, "48": 32, "49": 35, "50": 35, "51": 38, "52": 38, "53": 47, "54": 47, "55": 50, "56": 50, "57": 53, "58": 53, "59": 61, "60": 61, "61": 64, "62": 64, "63": 66, "64": 66, "65": 66, "66": 66, "67": 70, "68": 70, "69": 73, "70": 73, "71": 76, "72": 76, "73": 84, "74": 84, "75": 87, "76": 87, "77": 89, "78": 89, "79": 89, "80": 89, "81": 94, "82": 94, "83": 95, "84": 95, "85": 96, "86": 96, "87": 97, "88": 97, "89": 98, "90": 98, "91": 99, "92": 99, "93": 99, "94": 99, "95": 104, "96": 104, "97": 105, "98": 105, "99": 105, "100": 105, "101": 109, "102": 109, "103": 112, "104": 112, "105": 115, "106": 115, "107": 121, "108": 121, "109": 122, "110": 122, "111": 122, "112": 122, "113": 126, "114": 126, "115": 129, "116": 129, "117": 132, "118": 132, "119": 140, "120": 140, "121": 143, "122": 143, "123": 146, "124": 146, "125": 152, "126": 152, "127": 153, "128": 153, "129": 158, "130": 158, "131": 162, "132": 162, "133": 165, "134": 165, "135": 168, "136": 168, "137": 174, "138": 174, "139": 175, "140": 175, "141": 179, "142": 179, "143": 181, "144": 181, "145": 183, "146": 183, "147": 189, "148": 189, "149": 192, "150": 192, "151": 195, "152": 195, "153": 201, "154": 201, "155": 203, "156": 203, "157": 205, "158": 205, "159": 211, "160": 211, "161": 218, "162": 218, "163": 219, "164": 219, "165": 223, "166": 224, "167": 224, "168": 224, "169": 226, "170": 231, "171": 231, "172": 238, "173": 238, "174": 242, "175": 242, "181": 1, "185": 1, "186": 4, "187": 4, "188": 7, "189": 7, "195": 189}, "filename": "templates/settings/postprocessing.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
