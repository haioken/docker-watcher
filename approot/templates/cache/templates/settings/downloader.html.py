# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.6829824
_enable_loop = True
_template_filename = 'templates/settings/downloader.html'
_template_uri = 'templates/settings/downloader.html'
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
        __M_writer('\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/shared.js?v=002" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/downloader.js?v=001" type="text/javascript"></script>\n\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/shared.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/downloader.css?v=001" rel="stylesheet">\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <h1>')
        __M_writer(str(_('Download Clients')))
        __M_writer('</h1>\n\n            <h2>')
        __M_writer(str(_('Usenet')))
        __M_writer('</h2>\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    <select id="usenet_client" class="form-control select-sm">\n                        <option value="" selected="false">')
        __M_writer(str(_('Disabled')))
        __M_writer('</option>\n                        <option value="NzbGet">NzbGet</option>\n                        <option value="Sabnzbd">Sabnzbd</option>\n                        <option value="BlackHole">')
        __M_writer(str(_('Black Hole')))
        __M_writer('</option>\n                    </select>\n                </div>\n                <div id="usenet_client_settings" class="panel-body">\n                    <!-- NZBGET -->\n                    <div id="NzbGet" class="hidden" data-enabled="')
        __M_writer(str(config['Usenet']['NzbGet']['enabled']))
        __M_writer('">\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Host')))
        __M_writer('</label>\n                            <input type="text" data-id="host" class="form-control" placeholder="localhost" value="')
        __M_writer(str(config['Usenet']['NzbGet']['host']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Port')))
        __M_writer('</label>\n                            <input type="number" data-id="port" class="form-control" placeholder="6789" value="')
        __M_writer(str(config['Usenet']['NzbGet']['port']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('User Name')))
        __M_writer('</label>\n                            <input type="text" data-id="user" class="form-control" placeholder="" value="')
        __M_writer(str(config['Usenet']['NzbGet']['user']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Password')))
        __M_writer('</label>\n                            <input type="text" data-id="pass" class="form-control" placeholder="" value="')
        __M_writer(str(config['Usenet']['NzbGet']['pass']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Category')))
        __M_writer('</label>\n                            <input type="text" data-id="category" class="form-control" placeholder="Watcher" value="')
        __M_writer(str(config['Usenet']['NzbGet']['category']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Priority')))
        __M_writer('</label>\n                            <select data-id="priority" class="form-control" value="')
        __M_writer(str(config['Usenet']['NzbGet']['priority']))
        __M_writer('">\n                                <option value="Very Low">')
        __M_writer(str(_('Very Low')))
        __M_writer('</option>\n                                <option value="Low">')
        __M_writer(str(_('Low')))
        __M_writer('</option>\n                                <option value="Normal">')
        __M_writer(str(_('Normal')))
        __M_writer('</option>\n                                <option value="High">')
        __M_writer(str(_('High')))
        __M_writer('</option>\n                                <option value="Forced">')
        __M_writer(str(_('Forced')))
        __M_writer('</option>\n                            </select>\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Add Paused')))
        __M_writer('</label>\n                            <div class="input-group">\n                                <span class="input-group-addon box_box">\n                                    <i data-id="addpaused" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Usenet']['NzbGet']['addpaused']))
        __M_writer('"></i>\n                                </span>\n                                <span class="input-group-item form-control">\n                                    ')
        __M_writer(str(_('Add NZBs in Paused state.')))
        __M_writer('\n                                </span>\n                            </div>\n                        </div>\n                        <div class=\'col-md-12\'>\n                            <label>&nbsp;</label>\n                            <a class="btn btn-primary form-control" onclick="test_connection(event, this, \'NzbGet\')">\n                                <i class="mdi mdi-lan-pending"></i>\n                                ')
        __M_writer(str(_('Test Connection')))
        __M_writer('\n                            </a>\n                        </div>\n                    </div>\n                    <!-- SABNZBD -->\n                    <div id="Sabnzbd" class="hidden" data-enabled="')
        __M_writer(str(config['Usenet']['Sabnzbd']['enabled']))
        __M_writer('">\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Host')))
        __M_writer('</label>\n                            <input data-id="host" type="text" class="form-control" placeholder="localhost" value="')
        __M_writer(str(config['Usenet']['Sabnzbd']['host']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Port')))
        __M_writer('</label>\n                            <input type="number" data-id="port" class="form-control" placeholder="8080" value="')
        __M_writer(str(config['Usenet']['Sabnzbd']['port']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('API Key')))
        __M_writer('</label>\n                            <input type="text" data-id="api" class="form-control" placeholder="" value="')
        __M_writer(str(config['Usenet']['Sabnzbd']['api']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Category')))
        __M_writer('</label>\n                            <input type="text" data-id="category" class="form-control" placeholder="Watcher" value="')
        __M_writer(str(config['Usenet']['Sabnzbd']['category']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Priority')))
        __M_writer('</label>\n                            <select data-id="priority" class="form-control" value="')
        __M_writer(str(config['Usenet']['Sabnzbd']['priority']))
        __M_writer('">\n                                <option value="Paused">')
        __M_writer(str(_('Paused')))
        __M_writer('</option>\n                                <option value="Low">')
        __M_writer(str(_('Low')))
        __M_writer('</option>\n                                <option value="Normal">')
        __M_writer(str(_('Normal')))
        __M_writer('</option>\n                                <option value="High">')
        __M_writer(str(_('High')))
        __M_writer('</option>\n                                <option value="Forced">')
        __M_writer(str(_('Forced')))
        __M_writer('</option>\n                            </select>\n                        </div>\n                        <div class=\'col-md-12\'>\n                            <label>&nbsp;</label>\n                            <a class="btn btn-primary form-control" onclick="test_connection(event, this, \'Sabnzbd\')">\n                                <i class="mdi mdi-lan-pending"></i>\n                                ')
        __M_writer(str(_('Test Connection')))
        __M_writer('\n                            </a>\n                        </div>\n                    </div>\n                    <!-- BLACKHOLE -->\n                    <div id="BlackHole" class="hidden" data-enabled="')
        __M_writer(str(config['Usenet']['BlackHole']['enabled']))
        __M_writer('">\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Directory')))
        __M_writer('</label>\n                            <input data-id="directory" type="text" class="form-control" placeholder="/user/downloads/nzb" value="')
        __M_writer(str(config['Usenet']['BlackHole']['directory']))
        __M_writer('">\n                        </div>\n                        <div class=\'col-md-12\'>\n                            <label>&nbsp;</label>\n                            <a class="btn btn-primary form-control" onclick="test_connection(event, this, \'BlackHole\')">\n                                <i class="mdi mdi-lan-pending"></i>\n                                ')
        __M_writer(str(_('Test Connection')))
        __M_writer('\n                            </a>\n                        </div>\n                    </div>\n                </div>\n            </div>\n\n            <h2>')
        __M_writer(str(_('Torrent')))
        __M_writer('</h2>\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    <select id="torrent_client" class="form-control select-sm">\n                        <option value="" selected="false">')
        __M_writer(str(_('Disabled')))
        __M_writer('</option>\n                        <option value="DelugeRPC">Deluge Daemon</option>\n                        <option value="DelugeWeb">Deluge WebUI</option>\n                        <option value="rTorrentSCGI">rTorrent SCGI</option>\n                        <option value="rTorrentHTTP">rTorrent HTTP</option>\n                        <option value="Transmission">Transmission</option>\n                        <option value="QBittorrent">QBittorrent</option>\n                        <option value="BlackHole">')
        __M_writer(str(_('Black Hole')))
        __M_writer('</option>\n                    </select>\n                </div>\n                <div id="torrent_client_settings" class="panel-body">\n                    <!-- DELUGE RPC -->\n                    <div id="DelugeRPC" class="hidden" data-enabled="')
        __M_writer(str(config['Torrent']['DelugeRPC']['enabled']))
        __M_writer('">\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Host')))
        __M_writer('</label>\n                            <input type="text" data-id="host" class="form-control" placeholder="localhost" value="')
        __M_writer(str(config['Torrent']['DelugeRPC']['host']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Port')))
        __M_writer('</label>\n                            <input type="number" data-id="port" class="form-control" placeholder="58846" value="')
        __M_writer(str(config['Torrent']['DelugeRPC']['port']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('User Name')))
        __M_writer('</label>\n                            <input type="text" data-id="user" class="form-control" placeholder="" value="')
        __M_writer(str(config['Torrent']['DelugeRPC']['user']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Password')))
        __M_writer('</label>\n                            <input type="text" data-id="pass" class="form-control" placeholder="" value="')
        __M_writer(str(config['Torrent']['DelugeRPC']['pass']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Category')))
        __M_writer('</label>\n                            <input type="text" data-id="category" class="form-control" placeholder="Watcher" value="')
        __M_writer(str(config['Torrent']['DelugeRPC']['category']))
        __M_writer('" data-toggle="tooltip" title="')
        __M_writer(str(_('Must&nbsp;include&nbsp;only a&#8209;z&nbsp;0&#8209;9&nbsp;&#8209;&nbsp;_')))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Priority')))
        __M_writer('</label>\n                            <select data-id="priority" class="form-control" value="')
        __M_writer(str(config['Torrent']['DelugeRPC']['priority']))
        __M_writer('">\n                                <option value="Very Low">')
        __M_writer(str(_('Very Low')))
        __M_writer('</option>\n                                <option value="Low">')
        __M_writer(str(_('Low')))
        __M_writer('</option>\n                                <option value="Normal">')
        __M_writer(str(_('Normal')))
        __M_writer('</option>\n                                <option value="High">')
        __M_writer(str(_('High')))
        __M_writer('</option>\n                                <option value="Forced">')
        __M_writer(str(_('Forced')))
        __M_writer('</option>\n                            </select>\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Add Paused')))
        __M_writer('</label>\n                            <div class="input-group">\n                                <span class="input-group-addon box_box">\n                                    <i data-id="addpaused" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Torrent']['DelugeRPC']['addpaused']))
        __M_writer('"></i>\n                                </span>\n                                <span class="input-group-item form-control">\n                                    ')
        __M_writer(str(_('Add Torrents in Paused state.')))
        __M_writer('\n                                </span>\n                            </div>\n                        </div>\n                        <div class=\'col-md-12\'>\n                            <label>&nbsp;</label>\n                            <a class="btn btn-primary form-control" onclick="test_connection(event, this, \'DelugeRPC\')">\n                                <i class="mdi mdi-lan-pending"></i>\n                                ')
        __M_writer(str(_('Test Connection')))
        __M_writer('\n                            </a>\n                        </div>\n                    </div>\n                    <!-- DELUGE WEB -->\n                    <div id="DelugeWeb" class="hidden" data-enabled="')
        __M_writer(str(config['Torrent']['DelugeWeb']['enabled']))
        __M_writer('">\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Host')))
        __M_writer('</label>\n                            <input type="text" data-id="host" class="form-control" placeholder="localhost" value="')
        __M_writer(str(config['Torrent']['DelugeWeb']['host']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Port')))
        __M_writer('</label>\n                            <input type="number" data-id="port" class="form-control" placeholder="8112" value="')
        __M_writer(str(config['Torrent']['DelugeWeb']['port']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Password')))
        __M_writer('</label>\n                            <input type="text" data-id="pass" class="form-control" placeholder="" value="')
        __M_writer(str(config['Torrent']['DelugeWeb']['pass']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Category')))
        __M_writer('</label>\n                            <input type="text" data-id="category" class="form-control" placeholder="Watcher" value="')
        __M_writer(str(config['Torrent']['DelugeWeb']['category']))
        __M_writer('" data-toggle="tooltip" title="')
        __M_writer(str(_('Must&nbsp;include&nbsp;only a&#8209;z&nbsp;0&#8209;9&nbsp;&#8209;&nbsp;_')))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Priority')))
        __M_writer('</label>\n                            <select data-id="priority" class="form-control" value="')
        __M_writer(str(config['Torrent']['DelugeWeb']['priority']))
        __M_writer('">\n                                <option value="Very Low">')
        __M_writer(str(_('Very Low')))
        __M_writer('</option>\n                                <option value="Low">')
        __M_writer(str(_('Low')))
        __M_writer('</option>\n                                <option value="Normal">')
        __M_writer(str(_('Normal')))
        __M_writer('</option>\n                                <option value="High">')
        __M_writer(str(_('High')))
        __M_writer('</option>\n                                <option value="Forced">')
        __M_writer(str(_('Forced')))
        __M_writer('</option>\n                            </select>\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Add Paused')))
        __M_writer('</label>\n                            <div class="input-group">\n                                <span class="input-group-addon box_box">\n                                    <i data-id="addpaused" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Torrent']['DelugeWeb']['addpaused']))
        __M_writer('"></i>\n                                </span>\n                                <span class="input-group-item form-control">\n                                    ')
        __M_writer(str(_('Add Torrents in Paused state.')))
        __M_writer('\n                                </span>\n                            </div>\n                        </div>\n                        <div class=\'col-md-12\'>\n                            <label>&nbsp;</label>\n                            <a class="btn btn-primary form-control" onclick="test_connection(event, this, \'DelugeWeb\')">\n                                <i class="mdi mdi-lan-pending"></i>\n                                ')
        __M_writer(str(_('Test Connection')))
        __M_writer('\n                            </a>\n                        </div>\n                    </div>\n                    <!-- RTORRENT SCGI -->\n                    <div id="rTorrentSCGI" class="hidden" data-enabled="')
        __M_writer(str(config['Torrent']['rTorrentSCGI']['enabled']))
        __M_writer('">\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Host')))
        __M_writer('</label>\n                            <input type="text" data-id="host" class="form-control" placeholder="localhost" value="')
        __M_writer(str(config['Torrent']['rTorrentSCGI']['host']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Port')))
        __M_writer('</label>\n                            <input type="number" data-id="port" class="form-control" placeholder="5000" value="')
        __M_writer(str(config['Torrent']['rTorrentSCGI']['port']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Label')))
        __M_writer('</label>\n                            <input type="text" data-id="label" class="form-control" placeholder="Watcher" value="')
        __M_writer(str(config['Torrent']['rTorrentSCGI']['label']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Add Paused')))
        __M_writer('</label>\n                            <div class="input-group">\n                                <span class="input-group-addon box_box">\n                                    <i data-id="addpaused" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Torrent']['rTorrentSCGI']['addpaused']))
        __M_writer('"></i>\n                                </span>\n                                <span class="input-group-item form-control">\n                                    ')
        __M_writer(str(_('Add Torrents in Paused state.')))
        __M_writer('\n                                </span>\n                            </div>\n                        </div>\n                        <div class=\'col-md-12\'>\n                            <label>&nbsp;</label>\n                            <a class="btn btn-primary form-control" onclick="test_connection(event, this, \'rTorrentSCGI\')">\n                                <i class="mdi mdi-lan-pending"></i>\n                                ')
        __M_writer(str(_('Test Connection')))
        __M_writer('\n                            </a>\n                        </div>\n                    </div>\n                    <!-- RTORRENT HTTP -->\n                    <div id="rTorrentHTTP" class="hidden" data-enabled="')
        __M_writer(str(config['Torrent']['rTorrentHTTP']['enabled']))
        __M_writer('">\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('HTTP RPC Address')))
        __M_writer('</label>\n                            <input type="text" data-id="address" class="form-control" placeholder="localhost" value="')
        __M_writer(str(config['Torrent']['rTorrentHTTP']['address']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Label')))
        __M_writer('</label>\n                            <input type="text" data-id="label" class="form-control" placeholder="Watcher" value="')
        __M_writer(str(config['Torrent']['rTorrentHTTP']['label']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('User Name')))
        __M_writer('</label>\n                            <input type="text" data-id="user" class="form-control" placeholder="" value="')
        __M_writer(str(config['Torrent']['rTorrentHTTP']['user']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Password')))
        __M_writer('</label>\n                            <input type="text" data-id="pass" class="form-control" placeholder="" value="')
        __M_writer(str(config['Torrent']['rTorrentHTTP']['pass']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Add Paused')))
        __M_writer('</label>\n                            <div class="input-group">\n                                <span class="input-group-addon box_box">\n                                    <i data-id="addpaused" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Torrent']['rTorrentHTTP']['addpaused']))
        __M_writer('"></i>\n                                </span>\n                                <span class="input-group-item form-control">\n                                    ')
        __M_writer(str(_('Add Torrents in Paused state.')))
        __M_writer('\n                                </span>\n                            </div>\n                        </div>\n                        <div class=\'col-md-12\'>\n                            <label>&nbsp;</label>\n                            <a class="btn btn-primary form-control" onclick="test_connection(event, this, \'rTorrentHTTP\')">\n                                <i class="mdi mdi-lan-pending"></i>\n                                ')
        __M_writer(str(_('Test Connection')))
        __M_writer('\n                            </a>\n                        </div>\n                    </div>\n                    <!-- TRANSMISSION -->\n                    <div id="Transmission" class="hidden" data-enabled="')
        __M_writer(str(config['Torrent']['Transmission']['enabled']))
        __M_writer('">\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Host')))
        __M_writer('</label>\n                            <input type="text" data-id="host" class="form-control" placeholder="localhost" value="')
        __M_writer(str(config['Torrent']['Transmission']['host']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Port')))
        __M_writer('</label>\n                            <input type="number" data-id="port" class="form-control" placeholder="9091" value="')
        __M_writer(str(config['Torrent']['Transmission']['port']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('User Name')))
        __M_writer('</label>\n                            <input type="text" data-id="user" class="form-control" placeholder="" value="')
        __M_writer(str(config['Torrent']['Transmission']['user']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Password')))
        __M_writer('</label>\n                            <input type="text" data-id="pass" class="form-control" placeholder="" value="')
        __M_writer(str(config['Torrent']['Transmission']['pass']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Category')))
        __M_writer('</label>\n                            <input type="text" data-id="category" class="form-control" placeholder="Watcher" value="')
        __M_writer(str(config['Torrent']['Transmission']['category']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Priority')))
        __M_writer('</label>\n                            <select data-id="priority" class="form-control" value="')
        __M_writer(str(config['Torrent']['Transmission']['priority']))
        __M_writer('">\n                                <option value="Low">')
        __M_writer(str(_('Low')))
        __M_writer('</option>\n                                <option value="Normal">')
        __M_writer(str(_('Normal')))
        __M_writer('</option>\n                                <option value="High">')
        __M_writer(str(_('High')))
        __M_writer('</option>\n                            </select>\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Add Paused')))
        __M_writer('</label>\n                            <div class="input-group">\n                                <span class="input-group-addon box_box">\n                                    <i data-id="addpaused" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(config['Torrent']['Transmission']['addpaused']))
        __M_writer('"></i>\n                                </span>\n                                <span class="input-group-item form-control">\n                                    ')
        __M_writer(str(_('Add Torrents in Paused state.')))
        __M_writer('\n                                </span>\n                            </div>\n                        </div>\n                        <div class=\'col-md-12\'>\n                            <label>&nbsp;</label>\n                            <a class="btn btn-primary form-control" onclick="test_connection(event, this, \'Transmission\')">\n                                <i class="mdi mdi-lan-pending"></i>\n                                ')
        __M_writer(str(_('Test Connection')))
        __M_writer('\n                            </a>\n                        </div>\n                    </div>\n                    <!-- QBITTORRENT -->\n                    <div id="QBittorrent" class="hidden" data-enabled="')
        __M_writer(str(config['Torrent']['QBittorrent']['enabled']))
        __M_writer('">\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Host')))
        __M_writer('</label>\n                            <input type="text" data-id="host" class="form-control" placeholder="localhost" value="')
        __M_writer(str(config['Torrent']['QBittorrent']['host']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Port')))
        __M_writer('</label>\n                            <input type="number" data-id="port" class="form-control" placeholder="8080" value="')
        __M_writer(str(config['Torrent']['QBittorrent']['port']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('User Name')))
        __M_writer('</label>\n                            <input type="text" data-id="user" class="form-control" placeholder="" value="')
        __M_writer(str(config['Torrent']['QBittorrent']['user']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Password')))
        __M_writer('</label>\n                            <input type="text" data-id="pass" class="form-control" placeholder="" value="')
        __M_writer(str(config['Torrent']['QBittorrent']['pass']))
        __M_writer('">\n                        </div>\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Category')))
        __M_writer('</label>\n                            <input type="text" data-id="category" class="form-control" placeholder="Watcher" value="')
        __M_writer(str(config['Torrent']['QBittorrent']['category']))
        __M_writer('">\n                        </div>\n                        <div class=\'col-md-12\'>\n                            <label>&nbsp;</label>\n                            <a class="btn btn-primary form-control" onclick="test_connection(event, this, \'QBittorrent\')">\n                                <i class="mdi mdi-lan-pending"></i>\n                                ')
        __M_writer(str(_('Test Connection')))
        __M_writer('\n                            </a>\n                        </div>\n                    </div>\n                    <!-- BLACKHOLE -->\n                    <div id="BlackHole" class="hidden" data-enabled="')
        __M_writer(str(config['Torrent']['BlackHole']['enabled']))
        __M_writer('">\n                        <div class="col-md-6">\n                            <label>')
        __M_writer(str(_('Directory')))
        __M_writer('</label>\n                            <input type="text" data-id="directory" class="form-control" placeholder="/user/downloads/torrents" value="')
        __M_writer(str(config['Torrent']['BlackHole']['directory']))
        __M_writer('">\n                        </div>\n                        <div class=\'col-md-12\'>\n                            <label>&nbsp;</label>\n                            <a class="btn btn-primary form-control" onclick="test_connection(event, this, \'BlackHole\')">\n                                <i class="mdi mdi-lan-pending"></i>\n                                ')
        __M_writer(str(_('Test Connection')))
        __M_writer('\n                            </a>\n                        </div>\n                    </div>\n                </div>\n            </div>\n\n            <a id="save_settings" class="btn btn-success pull-right" onclick="save_settings(event, this)">\n                <i class="mdi mdi-content-save"></i>\n                ')
        __M_writer(str(_('Save Settings')))
        __M_writer('\n            </a>\n\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/settings/downloader.html", "line_map": {"16": 0, "26": 1, "27": 4, "28": 4, "29": 5, "30": 5, "31": 6, "32": 6, "33": 8, "34": 8, "35": 9, "36": 9, "37": 12, "38": 12, "39": 14, "40": 14, "41": 16, "42": 16, "43": 20, "44": 20, "45": 23, "46": 23, "47": 28, "48": 28, "49": 30, "50": 30, "51": 31, "52": 31, "53": 34, "54": 34, "55": 35, "56": 35, "57": 38, "58": 38, "59": 39, "60": 39, "61": 42, "62": 42, "63": 43, "64": 43, "65": 46, "66": 46, "67": 47, "68": 47, "69": 50, "70": 50, "71": 51, "72": 51, "73": 52, "74": 52, "75": 53, "76": 53, "77": 54, "78": 54, "79": 55, "80": 55, "81": 56, "82": 56, "83": 60, "84": 60, "85": 63, "86": 63, "87": 66, "88": 66, "89": 74, "90": 74, "91": 79, "92": 79, "93": 81, "94": 81, "95": 82, "96": 82, "97": 85, "98": 85, "99": 86, "100": 86, "101": 89, "102": 89, "103": 90, "104": 90, "105": 93, "106": 93, "107": 94, "108": 94, "109": 97, "110": 97, "111": 98, "112": 98, "113": 99, "114": 99, "115": 100, "116": 100, "117": 101, "118": 101, "119": 102, "120": 102, "121": 103, "122": 103, "123": 110, "124": 110, "125": 115, "126": 115, "127": 117, "128": 117, "129": 118, "130": 118, "131": 124, "132": 124, "133": 131, "134": 131, "135": 135, "136": 135, "137": 142, "138": 142, "139": 147, "140": 147, "141": 149, "142": 149, "143": 150, "144": 150, "145": 153, "146": 153, "147": 154, "148": 154, "149": 157, "150": 157, "151": 158, "152": 158, "153": 161, "154": 161, "155": 162, "156": 162, "157": 165, "158": 165, "159": 166, "160": 166, "161": 166, "162": 166, "163": 169, "164": 169, "165": 170, "166": 170, "167": 171, "168": 171, "169": 172, "170": 172, "171": 173, "172": 173, "173": 174, "174": 174, "175": 175, "176": 175, "177": 179, "178": 179, "179": 182, "180": 182, "181": 185, "182": 185, "183": 193, "184": 193, "185": 198, "186": 198, "187": 200, "188": 200, "189": 201, "190": 201, "191": 204, "192": 204, "193": 205, "194": 205, "195": 208, "196": 208, "197": 209, "198": 209, "199": 212, "200": 212, "201": 213, "202": 213, "203": 213, "204": 213, "205": 216, "206": 216, "207": 217, "208": 217, "209": 218, "210": 218, "211": 219, "212": 219, "213": 220, "214": 220, "215": 221, "216": 221, "217": 222, "218": 222, "219": 226, "220": 226, "221": 229, "222": 229, "223": 232, "224": 232, "225": 240, "226": 240, "227": 245, "228": 245, "229": 247, "230": 247, "231": 248, "232": 248, "233": 251, "234": 251, "235": 252, "236": 252, "237": 255, "238": 255, "239": 256, "240": 256, "241": 259, "242": 259, "243": 262, "244": 262, "245": 265, "246": 265, "247": 273, "248": 273, "249": 278, "250": 278, "251": 280, "252": 280, "253": 281, "254": 281, "255": 284, "256": 284, "257": 285, "258": 285, "259": 288, "260": 288, "261": 289, "262": 289, "263": 292, "264": 292, "265": 293, "266": 293, "267": 296, "268": 296, "269": 299, "270": 299, "271": 302, "272": 302, "273": 310, "274": 310, "275": 315, "276": 315, "277": 317, "278": 317, "279": 318, "280": 318, "281": 321, "282": 321, "283": 322, "284": 322, "285": 325, "286": 325, "287": 326, "288": 326, "289": 329, "290": 329, "291": 330, "292": 330, "293": 333, "294": 333, "295": 334, "296": 334, "297": 337, "298": 337, "299": 338, "300": 338, "301": 339, "302": 339, "303": 340, "304": 340, "305": 341, "306": 341, "307": 345, "308": 345, "309": 348, "310": 348, "311": 351, "312": 351, "313": 359, "314": 359, "315": 364, "316": 364, "317": 366, "318": 366, "319": 367, "320": 367, "321": 370, "322": 370, "323": 371, "324": 371, "325": 374, "326": 374, "327": 375, "328": 375, "329": 378, "330": 378, "331": 379, "332": 379, "333": 382, "334": 382, "335": 383, "336": 383, "337": 389, "338": 389, "339": 394, "340": 394, "341": 396, "342": 396, "343": 397, "344": 397, "345": 403, "346": 403, "347": 412, "348": 412, "354": 348}, "filename": "templates/settings/downloader.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
