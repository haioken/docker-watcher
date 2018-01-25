# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.609014
_enable_loop = True
_template_filename = 'templates/settings/indexers.html'
_template_uri = 'templates/settings/indexers.html'
_source_encoding = 'ascii'
_exports = ['render_indexer']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        head = context.get('head', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        config = context.get('config', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        def render_indexer(indexer):
            return render_render_indexer(context._locals(__M_locals),indexer)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/shared.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/indexers.css?v=001" rel="stylesheet">\n\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/shared.js?v=002" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/indexers.js?v=001" type="text/javascript"></script>\n\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n\n            <h1>')
        __M_writer(str(_('NewzNab Indexers')))
        __M_writer('</h1>\n            <form class="form-horizontal well" data-category="newznab">\n                <table class="table table-hover">\n                    <thead>\n                        <th></th>\n                        <th>')
        __M_writer(str(_('URL')))
        __M_writer('</th>\n                        <th>')
        __M_writer(str(_('API Key')))
        __M_writer('</th>\n                        <th></th>\n                    </thead>\n                    <tbody>\n')
        for indexer in config['NewzNab'].values():
            __M_writer('                        ')
            __M_writer(str(render_indexer(indexer)))
            __M_writer('\n')
        __M_writer('                    </tbody>\n                </table>\n                <div class=\'col-md-12\'>\n                    <button class="btn btn-primary" onclick="add_indexer(event, \'newznab\')">\n                        <i class="mdi mdi-plus"></i>\n                        ')
        __M_writer(str(_('Add Indexer')))
        __M_writer('\n                    </button>\n                </div>\n            </form>\n\n            <h1>')
        __M_writer(str(_('TorzNab Indexers')))
        __M_writer('</h1>\n            <form class="form-horizontal well" data-category="torznab">\n                <table class="table table-hover">\n                    <thead>\n                        <th></th>\n                        <th>')
        __M_writer(str(_('URL')))
        __M_writer('</th>\n                        <th>')
        __M_writer(str(_('API Key')))
        __M_writer('</th>\n                        <th></th>\n                    </thead>\n                    <tbody>\n')
        for indexer in config['TorzNab'].values():
            __M_writer('                        ')
            __M_writer(str(render_indexer(indexer)))
            __M_writer('\n')
        __M_writer('                    </tbody>\n                </table>\n                <div class=\'col-md-12\'>\n                    <button class="btn btn-primary" onclick="add_indexer(event, \'torznab\')">\n                        <i class="mdi mdi-plus"></i>\n                        ')
        __M_writer(str(_('Add Indexer')))
        __M_writer('\n                    </button>\n                </div>\n            </form>\n\n\n            <h1>')
        __M_writer(str(_('Torrent Indexers')))
        __M_writer('</h1>\n            <form class="form-horizontal well" data-category="torrent">\n                <div class="col-md-6">\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i class="mdi mdi-checkbox-blank-outline c_box" id="limetorrents" value="')
        __M_writer(str(config['Torrent']['limetorrents']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            LimeTorrents\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i class="mdi mdi-checkbox-blank-outline c_box" id="rarbg" value="')
        __M_writer(str(config['Torrent']['rarbg']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            Rarbg\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i class="mdi mdi-checkbox-blank-outline c_box" id="skytorrents" value="')
        __M_writer(str(config['Torrent']['skytorrents']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            SkyTorrents (')
        __M_writer(str(_('backlog only')))
        __M_writer(')\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i class="mdi mdi-checkbox-blank-outline c_box" id="thepiratebay" value="')
        __M_writer(str(config['Torrent']['thepiratebay']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ThePirateBay\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i class="mdi mdi-checkbox-blank-outline c_box" id="torrentdownloads" value="')
        __M_writer(str(config['Torrent']['torrentdownloads']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            TorrentDownloads\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i class="mdi mdi-checkbox-blank-outline c_box" id="torrentz2" value="')
        __M_writer(str(config['Torrent']['torrentz2']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            Torrentz2\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i class="mdi mdi-checkbox-blank-outline c_box" id="yts" value="')
        __M_writer(str(config['Torrent']['yts']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            YTS\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i class="mdi mdi-checkbox-blank-outline c_box" id="zooqle" value="')
        __M_writer(str(config['Torrent']['zooqle']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            Zooqle (')
        __M_writer(str(_('backlog only')))
        __M_writer(')\n                        </span>\n                    </div>\n                </div>\n            </form>\n\n            <a id="save_settings" class="btn btn-success pull-right" onclick="save_settings(event, this)">\n                <i class="mdi mdi-content-save"></i>\n                ')
        __M_writer(str(_('Save Settings')))
        __M_writer('\n            </a>\n        </div>\n\n        <textarea class="hidden" id="new_indexer">\n            ')
        __M_writer(str(render_indexer(['', '', 'False'])))
        __M_writer('\n        </textarea>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_indexer(context,indexer):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n\n    <tr>\n        <td>\n            <div class="input-group">\n                <div class="btn-group">\n                    <span class="input-group-addon box_box">\n                        <i class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(indexer[2]))
        __M_writer('"></i>\n                    </span>\n                    <span class="input-group-btn">\n                        <a class="btn btn-default" title="Test Indexer Connection" onclick="test_indexer(event, this)">\n                            <i class="mdi mdi-lan-pending"></i>\n                        </a>\n                    </span>\n                </div>\n            </div>\n        </td>\n        <td>\n            <input type="text" data-id="url" class="form-control" placeholder="http://www.indexer.com/" value="')
        __M_writer(str(indexer[0]))
        __M_writer('">\n        </td>\n        <td>\n            <input type="text" data-id="api" class="form-control" placeholder="123456789abcdef" value="')
        __M_writer(str(indexer[1]))
        __M_writer('">\n        </td>\n        <td>\n            <a class="btn btn-danger" onclick="remove_indexer(event, this)">\n                <i class="mdi mdi-delete"></i>\n            </a>\n        </td>\n    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/settings/indexers.html", "line_map": {"16": 0, "28": 30, "29": 36, "30": 36, "31": 38, "32": 38, "33": 39, "34": 39, "35": 41, "36": 41, "37": 42, "38": 42, "39": 46, "40": 46, "41": 49, "42": 49, "43": 54, "44": 54, "45": 55, "46": 55, "47": 59, "48": 60, "49": 60, "50": 60, "51": 62, "52": 67, "53": 67, "54": 72, "55": 72, "56": 77, "57": 77, "58": 78, "59": 78, "60": 82, "61": 83, "62": 83, "63": 83, "64": 85, "65": 90, "66": 90, "67": 96, "68": 96, "69": 101, "70": 101, "71": 111, "72": 111, "73": 121, "74": 121, "75": 124, "76": 124, "77": 131, "78": 131, "79": 141, "80": 141, "81": 151, "82": 151, "83": 161, "84": 161, "85": 171, "86": 171, "87": 174, "88": 174, "89": 182, "90": 182, "91": 187, "92": 187, "98": 1, "102": 1, "103": 8, "104": 8, "105": 19, "106": 19, "107": 22, "108": 22, "114": 108}, "filename": "templates/settings/indexers.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
