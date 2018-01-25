# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.7668777
_enable_loop = True
_template_filename = 'templates/system.html'
_template_uri = 'templates/system.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tasks = context.get('tasks', UNDEFINED)
        head = context.get('head', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        server_time = context.get('server_time', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        system = context.get('system', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/system.css?v=001" rel="stylesheet">\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/system.js?v=004" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/shared.js?v=002" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/lib/liteuploader.min.js?v=001" type="text/javascript"></script>\n\n        <meta name="tasks" content=\'')
        __M_writer(str(tasks))
        __M_writer('\'>\n        <meta name="server_time" content="')
        __M_writer(str(server_time[1]))
        __M_writer('">\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n\n            <h2>')
        __M_writer(str(_('System Information')))
        __M_writer('</h2>\n            <div class="col-md-12">\n                <div class="col-md-6">\n                    <div class="panel panel-primary">\n                        <div class="panel-heading">\n                            <i class="mdi mdi-clock"></i>')
        __M_writer(str(_('Server Time')))
        __M_writer('\n                        </div>\n                        <div id="server_time" class="panel-footer">\n                            ')
        __M_writer(str(server_time[0]))
        __M_writer('\n                        </div>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="panel panel-primary">\n                        <div class="panel-heading">\n                            <i class="mdi mdi-language-python"></i>')
        __M_writer(str(_('Watcher Directory')))
        __M_writer('\n                        </div>\n                        <div class="panel-footer">\n                            ')
        __M_writer(str(system['system']['path']))
        __M_writer('\n                        </div>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="panel panel-primary">\n                        <div class="panel-heading">\n                            <i class="mdi mdi-database"></i>')
        __M_writer(str(_('Database')))
        __M_writer('\n                            <span class="pull-right">[')
        __M_writer(str(system['database']['size']))
        __M_writer(' KB]</span>\n                        </div>\n                        <div class="panel-footer">\n                            ')
        __M_writer(str(system['database']['file']))
        __M_writer('\n                        </div>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="panel panel-primary">\n                        <div class="panel-heading">\n                            <i class="mdi mdi-settings"></i>')
        __M_writer(str(_('Config')))
        __M_writer('\n                        </div>\n                        <div class="panel-footer">\n                            ')
        __M_writer(str(system['config']['file']))
        __M_writer('\n                        </div>\n                    </div>\n                </div>\n                <div class="col-md-6">\n                    <div class="panel panel-primary">\n                        <div class="panel-heading">\n                            <i class="mdi mdi-console"></i>')
        __M_writer(str(_('Launch Arugments')))
        __M_writer('\n                        </div>\n                        <div class="panel-footer">\n                            [Python ')
        __M_writer(str(system['system']['version']))
        __M_writer(']\n                            ')
        __M_writer(str(' '.join(system['system']['arguments'])))
        __M_writer('\n                        </div>\n                    </div>\n                </div>\n            </div>\n\n            <h2>')
        __M_writer(str(_('Backup')))
        __M_writer('</h2>\n            <div class="col-md-12">\n                <a class="btn btn-default" data-toggle="modal" data-target="#modal_create_backup">\n                    <i class="mdi mdi-package-variant-closed"></i>\n                    ')
        __M_writer(str(_('Create Backup')))
        __M_writer('\n                </a>\n                <a class="btn btn-default" data-toggle="modal" data-target="#modal_restore_backup">\n                    <i class="mdi mdi-backup-restore"></i>\n                    ')
        __M_writer(str(_('Restore Backup')))
        __M_writer('\n                </a>\n            </div>\n            <br/>\n            <br/>\n\n            <h2>')
        __M_writer(str(_('Task Scheduler')))
        __M_writer('</h2>\n            <table id="tasks" class="table table-striped table-hover">\n                <thead>\n                    <tr>\n                        <th>')
        __M_writer(str(_('Enabled')))
        __M_writer('</th>\n                        <th>')
        __M_writer(str(_('Name')))
        __M_writer('</th>\n                        <th>')
        __M_writer(str(_('Frequency')))
        __M_writer('</th>\n                        <th>')
        __M_writer(str(_('Last Execution')))
        __M_writer('</th>\n                        <th>')
        __M_writer(str(_('Next Execution')))
        __M_writer('</th>\n                        <th class="center">')
        __M_writer(str(_('Execute Now')))
        __M_writer('</th>\n                    </tr>\n                </thead>\n                <tbody>\n\n                </tbody>\n            </table>\n\n            <div id="donate">\n                <a href="bitcoin:17BfQVGCsmHBNkVVbL1GxhhYFUMX2uytaT?label=Watcher">\n                <i class="mdi mdi-gift"></i>\n                <span>17BfQVGCsmHBNkVVbL1GxhhYFUMX2uytaT</span>\n            </div>\n        </div>\n\n        <div class="modal fade" id="modal_create_backup">\n            <div class="modal-dialog modal-sm">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <h4 class="modal-title">')
        __M_writer(str(_('Create Backup of Watcher?')))
        __M_writer('</h4>\n                    </div>\n                    <div class="modal-body">\n                        ')
        __M_writer(str(_('A backup will be made of your <b>database</b>, <b>posters</b>, and <b>config</b>.')))
        __M_writer('\n                        <div class="thinker_small">\n                            <i class="mdi mdi-circle-outline animated"></i>\n                        </div>\n                    </div>\n                    <div class="modal-footer">\n                        <div class="btn-group btn-group-justified">\n                            <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                            <a class="btn btn-success" onclick="create_backup(event, this)">')
        __M_writer(str(_('Create Backup')))
        __M_writer('</a>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n        <div class="modal fade" id="modal_restore_backup">\n            <div class="modal-dialog modal-sm">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <h4 class="modal-title">')
        __M_writer(str(_('Restore Backup of Watcher?')))
        __M_writer('</h4>\n                    </div>\n                    <div class="modal-body">\n                        <div class="text_content">\n                            ')
        __M_writer(str(_('Restoring a backup will overwrite your <b>database</b>, <b>posters</b>, and <b>config</b>.<br/>This cannot be undone.<br/>Watcher will automatically restart after backup has been restored.')))
        __M_writer('\n                            <br/>\n                            <div class="input-group">\n                                <label class="btn btn-default input-group-btn" for="zip_file">\n                                    <input id="zip_file" type="file" name="fileUpload" class="fileUpload" style="display:none;" onchange="_restore_zip_selected(this)"></input>\n                                    <i class="mdi mdi-zip-box"></i>\n                                    ')
        __M_writer(str(_('Select Backup Zip')))
        __M_writer('\n                                </label>\n                                <input id="zip_file_input" class="form-control input-group-item" disabled></input>\n                            </div>\n                        </div>\n                        <div class="thinker_small">\n                            <i class="mdi mdi-circle-outline animated"></i>\n                        </div>\n                        <div class="progress hidden">\n                            <div class="progress-bar"></div>\n                        </div>\n                    </div>\n                    <div class="modal-footer">\n                        <div class="btn-group btn-group-justified">\n                            <a class="btn btn-default" data-dismiss="modal">')
        __M_writer(str(_('Close')))
        __M_writer('</a>\n                            <a id="submit_restore_zip" class="btn btn-success disabled" onclick="upload_restore_zip(event, this)">')
        __M_writer(str(_('Restore Backup')))
        __M_writer('</a>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/system.html", "line_map": {"16": 0, "28": 1, "29": 4, "30": 4, "31": 5, "32": 5, "33": 6, "34": 6, "35": 7, "36": 7, "37": 8, "38": 8, "39": 10, "40": 10, "41": 11, "42": 11, "43": 14, "44": 14, "45": 17, "46": 17, "47": 22, "48": 22, "49": 25, "50": 25, "51": 32, "52": 32, "53": 35, "54": 35, "55": 42, "56": 42, "57": 43, "58": 43, "59": 46, "60": 46, "61": 53, "62": 53, "63": 56, "64": 56, "65": 63, "66": 63, "67": 66, "68": 66, "69": 67, "70": 67, "71": 73, "72": 73, "73": 77, "74": 77, "75": 81, "76": 81, "77": 87, "78": 87, "79": 91, "80": 91, "81": 92, "82": 92, "83": 93, "84": 93, "85": 94, "86": 94, "87": 95, "88": 95, "89": 96, "90": 96, "91": 115, "92": 115, "93": 118, "94": 118, "95": 125, "96": 125, "97": 126, "98": 126, "99": 136, "100": 136, "101": 140, "102": 140, "103": 146, "104": 146, "105": 160, "106": 160, "107": 161, "108": 161, "114": 108}, "filename": "templates/system.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
