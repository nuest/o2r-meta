import datetime
import sys
import os

__all__ = ['get_rel_path', 'get_prov', 'status_note', 'calculate_geo_bbox_union']


def get_rel_path(input_path, basedir):
    # this is the path for output and display, relative to --basedir flag
    output_path = os.path.relpath(os.path.join(input_path), basedir).replace('\\', '/')
    return output_path


def get_prov(path_file):
    return {'file': path_file, 'command': ' '.join((sys._getframe(1).f_globals['__name__'], sys._getframe(1).f_code.co_name))}


def status_note(msg, **kwargs):
    if type(msg) is list:
        msg_str_lst = []
        for n in msg:
            msg_str_lst.append(str(n))
        msg = ''.join(msg_str_lst)
    else:
        msg = str(msg)
    log_buffer = kwargs.get('b', None)
    debug_arg = kwargs.get('d', None)
    #date_txt = str(' {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    date_txt = str(' {:%Y%m%d.%H%M%S}'.format(datetime.datetime.now()))
    if debug_arg:
        debug_txt = ''.join(('[debug: ', sys._getframe(1).f_globals['__name__'], ' @ ', sys._getframe(1).f_code.co_name, ']'))
    else:
        debug_txt = ''
    if not log_buffer:
        print(''.join(('[o2rmeta]', debug_txt, date_txt, ' ', msg)))


def calculate_geo_bbox_union(coordinate_list):
    global is_debug
    if coordinate_list is None:
        #return [(0, 0), (0, 0), (0, 0), (0, 0)]
        return None
    else:
        try:
            min_x = 181.0
            min_y = 181.0
            max_x = -181.0
            max_y = -181.0
            # max =[181.0, 181.0, -181.0, -181.0]  # proper max has -90/90 & -180/180
            # todo: deal with international date line wrapping
            for n in coordinate_list:
                if n[0] < min_x:
                    min_x = n[0]
                if n[0] > max_x:
                    max_x = n[0]
                if n[1] < min_y:
                    min_y = n[1]
                if n[1] > max_y:
                    max_y = n[1]
            return [(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)]
        except Exception as exc:
            status_note(str(exc), d=True)
