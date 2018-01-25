# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.7404423
_enable_loop = True
_template_filename = 'templates/settings/plugins.html'
_template_uri = 'templates/settings/plugins.html'
_source_encoding = 'ascii'
_exports = ['render_plugins']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def render_plugins(kind):
            return render_render_plugins(context._locals(__M_locals),kind)
        navbar = context.get('navbar', UNDEFINED)
        head = context.get('head', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/shared.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/plugins.css?v=001" rel="stylesheet">\n\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/shared.js?v=002" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/plugins.js?v=001" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/lib/jquery.sortable.min.js?v=001" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <h1>')
        __M_writer(str(_('Plugins')))
        __M_writer('</h1>\n\n            <h3>')
        __M_writer(str(_('Added')))
        __M_writer('</h3>\n            <form class="form-horizontal well" data-category="added">\n                <ul class="sortable">\n                    ')
        __M_writer(str(render_plugins('added')))
        __M_writer('\n                </ul>\n            </form>\n\n            <h3>')
        __M_writer(str(_('Snatched')))
        __M_writer('</h3>\n            <form class="form-horizontal well" data-category="snatched">\n                <ul class="sortable">\n                    ')
        __M_writer(str(render_plugins('snatched')))
        __M_writer('\n                </ul>\n            </form>\n\n            <h3>')
        __M_writer(str(_('Finished')))
        __M_writer('</h3>\n            <form class="form-horizontal well" data-category="finished">\n                <ul class="sortable list-group">\n                    ')
        __M_writer(str(render_plugins('finished')))
        __M_writer('\n                </ul>\n            </form>\n\n            <div class="col-md-12 well">\n                ')
        __M_writer(str(_('See the Wiki for plugin instruction.')))
        __M_writer('\n                <a href="https://github.com/nosmokingbandit/Watcher3/wiki/Plugins", target="_blank" rel="noopener">\n                    <i class="mdi mdi-help-circle-outline"></i>\n                </a>\n\n            </div>\n\n            <a id="save_settings" class="btn btn-success pull-right" onclick="save_settings(event, this)">\n                <i class="mdi mdi-content-save"></i>\n                ')
        __M_writer(str(_('Save Settings')))
        __M_writer('\n            </a>\n\n        </div>\n\n        <textarea id="template_config" class="hidden">\n            <div class="modal fade" id="modal_plugin_conf" data-folder="{folder}" data-filename="{filename}">\n                <div class="modal-dialog modal-lg">\n                    <div class="modal-content">\n                        <div class="modal-header">\n                            <h4 class="modal-title">{name}</h4>\n                        </div>\n                        <div class="modal-body">\n                            {config}\n                        </div>\n                        <div class="modal-footer">\n                            <div class="btn-group btn-group-justified">\n                                <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                                <a class="btn btn-success" onclick="save_plugin_conf(event, this)">')
        __M_writer(str(_('Save Config')))
        __M_writer('</a>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </textarea>\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_plugins(context,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        plugins = context.get('plugins', UNDEFINED)
        config = context.get('config', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')

        fid = 0
        
        
        __M_writer('\n')
        for plugin in plugins[kind]:
            __M_writer('        ')

            name = plugin[0]
            enabled, sort = config[kind].get(name, (False, 900+fid))
            fid += 1
            
            
            __M_writer('\n        <li id="')
            __M_writer(str(kind))
            __M_writer(str(fid))
            __M_writer('" class="list-group-item" data-name="')
            __M_writer(str(plugin[0]))
            __M_writer('" data-sort="')
            __M_writer(str(sort))
            __M_writer('">\n            <i class="mdi mdi-drag-horizontal sortable_handle"></i>\n            <i class="mdi mdi-checkbox-blank-outline c_box" value="')
            __M_writer(str(enabled))
            __M_writer('"></i>\n            ')
            __M_writer(str(name[:-3]))
            __M_writer('\n')
            if plugin[1]:
                __M_writer('            <i class="mdi mdi-settings" onclick="edit_plugin_conf(event, this, \'')
                __M_writer(str(kind))
                __M_writer("', '")
                __M_writer(str(plugin[1]))
                __M_writer('\')"></i>\n')
            __M_writer('        </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/settings/plugins.html", "line_map": {"16": 0, "27": 20, "28": 25, "29": 25, "30": 26, "31": 26, "32": 27, "33": 27, "34": 29, "35": 29, "36": 30, "37": 30, "38": 31, "39": 31, "40": 34, "41": 34, "42": 36, "43": 36, "44": 38, "45": 38, "46": 41, "47": 41, "48": 45, "49": 45, "50": 48, "51": 48, "52": 52, "53": 52, "54": 55, "55": 55, "56": 60, "57": 60, "58": 69, "59": 69, "60": 86, "61": 86, "62": 87, "63": 87, "69": 1, "75": 1, "76": 2, "80": 4, "81": 5, "82": 6, "83": 6, "89": 10, "90": 11, "91": 11, "92": 11, "93": 11, "94": 11, "95": 11, "96": 11, "97": 13, "98": 13, "99": 14, "100": 14, "101": 15, "102": 16, "103": 16, "104": 16, "105": 16, "106": 16, "107": 18, "113": 107}, "filename": "templates/settings/plugins.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
