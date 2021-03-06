# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.5148454
_enable_loop = True
_template_filename = 'templates/settings/server.html'
_template_uri = 'templates/settings/server.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        languages = context.get('languages', UNDEFINED)
        head = context.get('head', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        config = context.get('config', UNDEFINED)
        version = context.get('version', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        themes = context.get('themes', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/shared.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/server.css?v=001" rel="stylesheet">\n\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/shared.js?v=002" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/server.js?v=001" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n\n            <h1>')
        __M_writer(str(_('Server')))
        __M_writer('</h1>\n            <form class="form-horizontal well" data-category="server">\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Host')))
        __M_writer(' *</label>\n                    <input type="text" id="serverhost" class="form-control" placeholder="0.0.0.0" value="')
        __M_writer(str(config['serverhost']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Port')))
        __M_writer(' *</label>\n                    <input type="number" id="serverport" class="form-control" placeholder="9090" min="0" value="')
        __M_writer(str(config['serverport']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Custom Webroot')))
        __M_writer(' *</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="customwebroot" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['customwebroot']))
        __M_writer('"></i>\n                        </span>\n                        <input type="text" id="customwebrootpath" class="form-control" value="')
        __M_writer(str(config['customwebrootpath']))
        __M_writer('">\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Api Key')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <input type="text" id="apikey" class="form-control" value="')
        __M_writer(str(config['apikey']))
        __M_writer('">\n                        <span class="input-group-btn">\n                            <a class="btn btn-primary" onclick="new_key(event)">\n                                <i class="mdi mdi-key-variant"></i>\n                                ')
        __M_writer(str(_('New Key')))
        __M_writer('\n                            </a>\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Keep [X] Days of Logs')))
        __M_writer(' *</label>\n                    <input type="number" id="keeplog" class="form-control" min="0" placeholder="3" value="')
        __M_writer(str(config['keeplog']))
        __M_writer('">\n                </div>\n\n\n            </form>\n\n            <h1>')
        __M_writer(str(_('Security')))
        __M_writer('</h1>\n            <form class="form-horizontal well" data-category="server">\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Password-protect Web-UI')))
        __M_writer(' *</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="authrequired" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['authrequired']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                                ')
        __M_writer(str(_('Require login to access Web-UI.')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-3">\n                    <label>')
        __M_writer(str(_('User Name')))
        __M_writer('</label>\n                    <input type="text" id="authuser" class="form-control" value="')
        __M_writer(str(config['authuser']))
        __M_writer('">\n                </div>\n                <div class="col-md-3">\n                    <label>')
        __M_writer(str(_('Password')))
        __M_writer('</label>\n                    <input type="text" id="authpass" class="form-control" value="')
        __M_writer(str(config['authpass']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('SSL Cert')))
        __M_writer(' *</label>\n                    <input type="text" id="ssl_cert" class="form-control" placeholder="/path/to/cert.crt" value="')
        __M_writer(str(config['ssl_cert']))
        __M_writer('">\n                </div>\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('SSL Key')))
        __M_writer(' *</label>\n                    <input type="text" id="ssl_key" class="form-control" placeholder="/path/to/privatekey.key" value="')
        __M_writer(str(config['ssl_key']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Verify Remote SSL Certificates')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="verifyssl" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['verifyssl']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Disable for non-functional SSL installs.')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n            </form>\n\n            <h1>')
        __M_writer(str(_('Interface')))
        __M_writer('</h1>\n            <form class="form-horizontal well" data-category="server">\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Theme')))
        __M_writer('</label>\n                    <select class="form-control select-sm" id="uitheme" value="')
        __M_writer(str(config['uitheme'] or 'Default'))
        __M_writer('">\n')
        for i in themes:
            __M_writer('                        <option value="')
            __M_writer(str(i))
            __M_writer('">')
            __M_writer(str(i))
            __M_writer('</option>\n')
        __M_writer('                    </select>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Open Browser')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="launchbrowser" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['launchbrowser']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Open Browser when launching Watcher.')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <label>Hide Finished Movies</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="hidefinished" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['hidefinished']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            Hide Finished movies in library\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Language')))
        __M_writer('</label>\n                    <select class="form-control select-sm" id="language" value="')
        __M_writer(str(config['language'] or 'en'))
        __M_writer('">\n')
        for i in languages:
            __M_writer('                        <option value="')
            __M_writer(str(i))
            __M_writer('">')
            __M_writer(str(i))
            __M_writer('</option>\n')
        __M_writer('                    </select>\n                </div>\n            </form>\n            <h1>')
        __M_writer(str(_('Updates')))
        __M_writer('</h1>\n            <form class="form-horizontal well" data-category="server">\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Check for Updates')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="checkupdates" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['checkupdates']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Automatically check for updates.')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Update Check Frequency')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <input type="number" id="checkupdatefrequency" class="form-control" min="4" placeholder="24 "value="')
        __M_writer(str(config['checkupdatefrequency']))
        __M_writer('">\n                        <span class="input-group-addon">\n                            ')
        __M_writer(str(_('Hours')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Install Updates')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="installupdates" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['installupdates']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Automatically install updates.')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Check for Updates')))
        __M_writer('</label>\n                    <a class="btn btn-primary btn-block" onclick="update_check(event, this)">\n                        <i class="mdi mdi-update"></i>\n                        ')
        __M_writer(str(_('Check for Updates Now')))
        __M_writer('\n                    </a>\n                </div>\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Current Version Hash')))
        __M_writer('</label>\n                    <span class="input-group-item form-control">\n                        <a href="https://github.com/nosmokingbandit/Watcher3/commit/')
        __M_writer(str(version))
        __M_writer('">\n                            ')
        __M_writer(str(version))
        __M_writer('\n                        </a>\n                    </span>\n                </div>\n                <div class="col-md-6">\n                    <label>Git Binary Path</label>\n                    <input type="text" id="gitpath" class="form-control" placeholder="/path/to/git" value="')
        __M_writer(str(config['gitpath']))
        __M_writer('">\n                </div>\n            </form>\n\n            <h1>')
        __M_writer(str(_('Proxy')))
        __M_writer('</h1>\n            <form class="form-horizontal well" data-category="proxy">\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Enable Proxy')))
        __M_writer('</label>\n                    <div class="input-group">\n                        <span class="input-group-addon box_box">\n                            <i id="enabled" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Proxy']['enabled']))
        __M_writer('"></i>\n                        </span>\n                        <span class="input-group-item form-control">\n                            ')
        __M_writer(str(_('Use proxy when connecting to Indexers.')))
        __M_writer('\n                        </span>\n                    </div>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Proxy Protocol')))
        __M_writer('</label>\n                    <select class="form-control select-sm" id="type" value="')
        __M_writer(str(config['Proxy']['type']))
        __M_writer('">\n                        <option value="http(s)">HTTP(s)</option>\n                        <option value="socks4">SOCKS4</option>\n                        <option value="socks5">SOCKS5</option>\n                    </select>\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Address')))
        __M_writer('</label>\n                    <input type="text" id="host" class="form-control" placeholder="https://1.2.3.4" value="')
        __M_writer(str(config['Proxy']['host']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Port')))
        __M_writer('</label>\n                    <input type="number" id="port" class="form-control" min="0" placeholder="1234" value="')
        __M_writer(str(config['Proxy']['port']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('User Name')))
        __M_writer('</label>\n                    <input type="text" id="user" class="form-control" placeholder="Rick_Sanchez" value="')
        __M_writer(str(config['Proxy']['user']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-6">\n                    <label>')
        __M_writer(str(_('Password')))
        __M_writer('</label>\n                    <input type="text" id="pass" class="form-control" placeholder="rickest_rick_c-137" value="')
        __M_writer(str(config['Proxy']['pass']))
        __M_writer('">\n                </div>\n\n                <div class="col-md-12">\n                    <label>')
        __M_writer(str(_('Whitelist')))
        __M_writer('</label>\n                    <input type="text" id="whitelist" class="form-control" placeholder="http://localhost:5075, http://localhost:5060" value="')
        __M_writer(str(config['Proxy']['whitelist']))
        __M_writer('" data-toggle="tooltip" title="')
        __M_writer(str(_('Separate URLs with commas')))
        __M_writer('">\n                </div>\n\n            </form>\n            <p>\n                * ')
        __M_writer(str(_('Requires Restart')))
        __M_writer('\n                <br/><br/>\n            </p>\n\n            <div class="btn-group">\n                <a class="btn btn-warning" data-toggle="modal" data-target="#modal_restart">\n                    <i class="mdi mdi-restart"></i>\n                    ')
        __M_writer(str(_('Restart')))
        __M_writer('\n                </a>\n                <a class="btn btn-danger" data-toggle="modal" data-target="#modal_shutdown">\n                    <i class="mdi mdi-power"></i>\n                    ')
        __M_writer(str(_('Shut Down')))
        __M_writer('\n                </a>\n            </div>\n            <a id="save_settings" class="btn btn-success pull-right" onclick="save_settings(event, this)">\n                <i class="mdi mdi-content-save"></i>\n                ')
        __M_writer(str(_('Save Settings')))
        __M_writer('\n            </a>\n        </div>\n\n        <span id="git_url" class="hidden">https://github.com/nosmokingbandit/watcher3</span>\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/settings/server.html", "line_map": {"16": 0, "29": 1, "30": 4, "31": 4, "32": 5, "33": 5, "34": 6, "35": 6, "36": 8, "37": 8, "38": 9, "39": 9, "40": 12, "41": 12, "42": 15, "43": 15, "44": 19, "45": 19, "46": 20, "47": 20, "48": 24, "49": 24, "50": 25, "51": 25, "52": 29, "53": 29, "54": 32, "55": 32, "56": 34, "57": 34, "58": 39, "59": 39, "60": 41, "61": 41, "62": 45, "63": 45, "64": 52, "65": 52, "66": 53, "67": 53, "68": 59, "69": 59, "70": 62, "71": 62, "72": 65, "73": 65, "74": 68, "75": 68, "76": 74, "77": 74, "78": 75, "79": 75, "80": 78, "81": 78, "82": 79, "83": 79, "84": 83, "85": 83, "86": 84, "87": 84, "88": 87, "89": 87, "90": 88, "91": 88, "92": 92, "93": 92, "94": 95, "95": 95, "96": 98, "97": 98, "98": 104, "99": 104, "100": 108, "101": 108, "102": 109, "103": 109, "104": 110, "105": 111, "106": 111, "107": 111, "108": 111, "109": 111, "110": 113, "111": 117, "112": 117, "113": 120, "114": 120, "115": 123, "116": 123, "117": 131, "118": 131, "119": 140, "120": 140, "121": 141, "122": 141, "123": 142, "124": 143, "125": 143, "126": 143, "127": 143, "128": 143, "129": 145, "130": 148, "131": 148, "132": 152, "133": 152, "134": 155, "135": 155, "136": 158, "137": 158, "138": 164, "139": 164, "140": 166, "141": 166, "142": 168, "143": 168, "144": 174, "145": 174, "146": 177, "147": 177, "148": 180, "149": 180, "150": 186, "151": 186, "152": 189, "153": 189, "154": 193, "155": 193, "156": 195, "157": 195, "158": 196, "159": 196, "160": 202, "161": 202, "162": 206, "163": 206, "164": 210, "165": 210, "166": 213, "167": 213, "168": 216, "169": 216, "170": 222, "171": 222, "172": 223, "173": 223, "174": 231, "175": 231, "176": 232, "177": 232, "178": 236, "179": 236, "180": 237, "181": 237, "182": 241, "183": 241, "184": 242, "185": 242, "186": 246, "187": 246, "188": 247, "189": 247, "190": 251, "191": 251, "192": 252, "193": 252, "194": 252, "195": 252, "196": 257, "197": 257, "198": 264, "199": 264, "200": 268, "201": 268, "202": 273, "203": 273, "209": 203}, "filename": "templates/settings/server.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
