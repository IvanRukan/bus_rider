import json


def json_decoder(js):
    return json.loads(js)


def checker(user_input):
    buses_id = {}
    stop_names_all = {}
    start_stops = []
    finnish_stops = []
    transfer_stops = []
    stop_names_wrong = []
    o_stops = []
    for each_o_stop in user_input:
        if each_o_stop['stop_type'] == 'O':
            o_stops.append(each_o_stop['stop_name'])
    for each_dict in user_input:
        buses_id[each_dict['bus_id']] = ''
        stop_names_all[each_dict['stop_name']] = ''
        if each_dict['stop_type'] == 'S':
            start_stops.append(each_dict['stop_name'])
        if each_dict['stop_type'] == 'F':
            finnish_stops.append(each_dict['stop_name'])
    for stop in stop_names_all.keys():
        content = []
        for each_stop in user_input:
            if stop == each_stop['stop_name']:
                content.append(each_stop['stop_type'])
        stop_names_all[stop] = content
    for trans_stop in stop_names_all.keys():
        if len(stop_names_all[trans_stop]) > 1:
            transfer_stops.append(trans_stop)
    for stop in o_stops:
        if stop in transfer_stops or stop in finnish_stops or stop in start_stops:
            stop_names_wrong.append(stop)

    if stop_names_wrong:
        print('On demand stop test:')
        print('Wrong stop types: ', sorted(stop_names_wrong))
    else:
        print('On demand stop test:')
        print('OK')


def printer(result):
    pass


printer(checker(json_decoder(input())))
