# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516862707.5912006
_enable_loop = True
_template_filename = 'templates/settings/quality.html'
_template_uri = 'templates/settings/quality.html'
_source_encoding = 'ascii'
_exports = ['generate_profile']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        head = context.get('head', UNDEFINED)
        url_base = context.get('url_base', UNDEFINED)
        config = context.get('config', UNDEFINED)
        navbar = context.get('navbar', UNDEFINED)
        sources = context.get('sources', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        def generate_profile(name,profile):
            return render_generate_profile(context._locals(__M_locals),name,profile)
        __M_writer = context.writer()

        user_profiles = {k: v for k, v in config['Profiles'].items() if k != 'Default'}
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['v','user_profiles','k'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        __M_writer('\n\n\n<!DOCTYPE HTML5>\n<html>\n    <head>\n        ')
        __M_writer(str(head))
        __M_writer('\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/shared.css?v=001" rel="stylesheet">\n        <link href="')
        __M_writer(str(url_base))
        __M_writer('/static/css/settings/quality.css?v=001" rel="stylesheet">\n\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/shared.js?v=002" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/settings/quality.js?v=001" type="text/javascript"></script>\n        <script src="')
        __M_writer(str(url_base))
        __M_writer('/static/js/lib/jquery.sortable.min.js?v=001" type="text/javascript"></script>\n    </head>\n    <body>\n        ')
        __M_writer(str(navbar))
        __M_writer('\n        <div class="container-fluid">\n            <h1>')
        __M_writer(str(_('Quality Profiles')))
        __M_writer("</h1>\n            <form id='profiles'>\n                ")
        __M_writer(str(generate_profile("Default", config['Profiles']['Default'])))
        __M_writer('\n\n')
        for name, profile in user_profiles.items():
            __M_writer('                ')
            __M_writer(str(generate_profile(name, profile)))
            __M_writer('\n')
        __M_writer('            </form>\n\n            <div class=\'col-md-12\' id="add_profile">\n                <a class="btn btn-primary" onclick="add_profile(event)">\n                    <i class="mdi mdi-plus"></i>\n                    ')
        __M_writer(str(_('Add Profile')))
        __M_writer('\n                </a>\n            </div>\n\n            <h1>')
        __M_writer(str(_('Sources')))
        __M_writer('</h1>\n            <form class="form-horizontal well" data-category="sources">\n                <span><b>')
        __M_writer(str(_('Specify acceptable size ranges (in MegaBytes) for source media.')))
        __M_writer('</b></span>\n                <table class="table table-hover">\n                    <thead>\n                        <tr>\n                            <th></th>\n                            <th>')
        __M_writer(str(_('Min Size')))
        __M_writer('</th>\n                            <th>')
        __M_writer(str(_('Max Size')))
        __M_writer('</th>\n                        </tr>\n                    </thead>\n                    <tbody>\n')
        for src in sources:
            __M_writer('                        ')

            v = config['Sources'][src]
                                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['v'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\n                        <tr id="')
            __M_writer(str(src))
            __M_writer('">\n                            <td>')
            __M_writer(str(src))
            __M_writer('</td>\n                            <td>\n                                <input type="number" class="input-sm form-control" data-range="min" min="0" value=')
            __M_writer(str(v['min']))
            __M_writer('>\n                            </td>\n                            <td>\n                                <input type="number" class="input-sm form-control" data-range="max" min="0" value=')
            __M_writer(str(v['max']))
            __M_writer('>\n                            </td>\n                        </tr>\n')
        __M_writer('                    </tbody>\n                </table>\n            </form>\n\n            <h2>')
        __M_writer(str(_('Aliases')))
        __M_writer('</h2>\n            <form class="form-horizontal well" data-category="aliases">\n                <span><b>')
        __M_writer(str(_('Keywords used to determine source media')))
        __M_writer('</b></span>\n                <br/>\n                <br/>\n                <table id="aliases" class="table table-hover" data-toggle="tooltip"title="')
        __M_writer(str(_('Separate Keywords with commas')))
        __M_writer('">\n                    <tbody>\n')
        for name, alias in config['Aliases'].items():
            __M_writer('                        <tr>\n                            <td>')
            __M_writer(str(name))
            __M_writer('</td>\n                            <td>\n                                <input type="text" id="')
            __M_writer(str(name))
            __M_writer('" class="input-sm form-control" value="')
            __M_writer(str(', '.join(alias)))
            __M_writer('">\n                            </td>\n                        </tr>\n')
        __M_writer('                    </tbody>\n                </table>\n            </form>\n\n            <a id="save_settings" class="btn btn-success pull-right" onclick="save_settings(event, this)">\n                <i class="mdi mdi-content-save"></i>\n                ')
        __M_writer(str(_('Save Settings')))
        __M_writer('\n            </a>\n        </div>\n\n        <textarea id="profile_template" class="hidden">\n            ')
        __M_writer(str(generate_profile("", {'Sources': {'BluRay-1080P': [True, 1], 'BluRay-4K': [False, 0], 'BluRay-720P': [True, 2], 'CAM-SD': [False, 13], 'DVD-SD': [False, 9], 'Screener-1080P': [False, 10], 'Screener-720P': [False, 11], 'Telesync-SD': [False, 12], 'WebDL-1080P': [True, 4], 'WebDL-4K': [False, 3], 'WebDL-720P': [True, 5], 'WebRip-1080P': [True, 7], 'WebRip-4K': [False, 6], 'WebRip-720P': [True, 8]}, 'ignoredwords': 'subs,german,dutch,french,truefrench,danish,swedish,spanish,italian,korean,dubbed,swesub,korsub,dksubs,vain,HC,blurred', 'preferredwords': '', 'prefersmaller': False, 'requiredwords': '', 'scoretitle': True})))
        __M_writer('\n        </textarea>\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_generate_profile(context,name,profile):
    __M_caller = context.caller_stack._push_frame()
    try:
        sources = context.get('sources', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="')
        __M_writer(str(name))
        __M_writer('" class="well quality_profile">\n\n')
        if name == 'Default':
            __M_writer('        <div class="col-md-12">\n            <h2>')
            __M_writer(str(_('Default')))
            __M_writer('</h2>\n            <input type="hidden" id="name" value="Default">\n        </div>\n')
        else:
            __M_writer('\n            <div class="col-md-6 input-group">\n                <input type="text" id="name" class="form-control" value="')
            __M_writer(str(name))
            __M_writer('">\n                <span class="input-group-btn">\n                    <a class="btn btn-danger pull-right" onclick="delete_profile(event, this)">\n                        <i class="mdi mdi-delete delete_profile"></i>\n                    </a>\n                </span>\n            </div>\n')
        __M_writer('\n        <div class="col-md-6">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    ')
        __M_writer(str(_('Sources')))
        __M_writer('\n                </div>\n                <div class="panel-body">\n                    <ul class="sources sortable">\n')
        for src in sources:
            __M_writer('                        <li class="source" data-source="')
            __M_writer(str(src))
            __M_writer('" data-sort="')
            __M_writer(str(profile['Sources'].get(src, [None, 99])[1]))
            __M_writer('">\n                            <i class="mdi mdi-drag-horizontal sortable_handle"></i>\n                            <i class="mdi mdi-checkbox-blank-outline c_box" value="')
            __M_writer(str(profile['Sources'].get(src, [False, None])[0]))
            __M_writer('"></i>\n                            ')
            __M_writer(str(src))
            __M_writer('\n                        </li>\n')
        __M_writer('                    </ul>\n                </div>\n            </div>\n        </div>\n\n        <div class="col-md-6">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    ')
        __M_writer(str(_('Filters')))
        __M_writer('\n                </div>\n                <div class="panel-body" data-sub-category="filters" data-toggle="tooltip" title="')
        __M_writer(str(_('Group words with ampersands and split groups with commas')))
        __M_writer('">\n                    <label>')
        __M_writer(str(_('Required Words')))
        __M_writer('</label>\n                    <input type="text" id="requiredwords" class="form-control" value="')
        __M_writer(str(profile['requiredwords']))
        __M_writer('">\n\n                    <label>')
        __M_writer(str(_('Preferred Words')))
        __M_writer('</label>\n                    <input type="text" id="preferredwords" class="form-control" placeholder=\'this&is&a&group, one, two, three\' value="')
        __M_writer(str(profile['preferredwords']))
        __M_writer('">\n\n                    <label>')
        __M_writer(str(_('Ignored Words')))
        __M_writer('</label>\n                    <input type="text" id="ignoredwords" class="form-control" value="')
        __M_writer(str(profile['ignoredwords']))
        __M_writer('">\n\n                </div>\n            </div>\n        </div>\n\n        <div class="col-md-6">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    ')
        __M_writer(str(_('Misc.')))
        __M_writer('\n                </div>\n                <div class="panel-body" data-sub-category="misc">\n                    <ul>\n                        <li>\n                            <i id="scoretitle" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(profile['scoretitle']))
        __M_writer('"></i>\n                            ')
        __M_writer(str(_('Score and filter release titles')))
        __M_writer('\n                        </li>\n                        <li>\n                            <i id="prefersmaller" class="mdi mdi-checkbox-blank-outline c_box" value="')
        __M_writer(str(profile['prefersmaller']))
        __M_writer('"></i>\n                            ')
        __M_writer(str(_('Prefer smaller file sizes')))
        __M_writer('\n                        </li>\n                    </ul>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "templates/settings/quality.html", "line_map": {"16": 0, "29": 1, "35": 3, "36": 83, "37": 89, "38": 89, "39": 90, "40": 90, "41": 91, "42": 91, "43": 93, "44": 93, "45": 94, "46": 94, "47": 95, "48": 95, "49": 98, "50": 98, "51": 100, "52": 100, "53": 102, "54": 102, "55": 104, "56": 105, "57": 105, "58": 105, "59": 107, "60": 112, "61": 112, "62": 116, "63": 116, "64": 118, "65": 118, "66": 123, "67": 123, "68": 124, "69": 124, "70": 128, "71": 129, "72": 129, "78": 131, "79": 132, "80": 132, "81": 133, "82": 133, "83": 135, "84": 135, "85": 138, "86": 138, "87": 142, "88": 146, "89": 146, "90": 148, "91": 148, "92": 151, "93": 151, "94": 153, "95": 154, "96": 155, "97": 155, "98": 157, "99": 157, "100": 157, "101": 157, "102": 161, "103": 167, "104": 167, "105": 172, "106": 172, "112": 5, "118": 5, "119": 6, "120": 6, "121": 8, "122": 9, "123": 10, "124": 10, "125": 13, "126": 14, "127": 16, "128": 16, "129": 24, "130": 28, "131": 28, "132": 32, "133": 33, "134": 33, "135": 33, "136": 33, "137": 33, "138": 35, "139": 35, "140": 36, "141": 36, "142": 39, "143": 47, "144": 47, "145": 49, "146": 49, "147": 50, "148": 50, "149": 51, "150": 51, "151": 53, "152": 53, "153": 54, "154": 54, "155": 56, "156": 56, "157": 57, "158": 57, "159": 66, "160": 66, "161": 71, "162": 71, "163": 72, "164": 72, "165": 75, "166": 75, "167": 76, "168": 76, "174": 168}, "filename": "templates/settings/quality.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
