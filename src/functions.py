import operator


def remove_labels_from(data_list):
    deleted_labels = []
    for i in data_list:
        deleted_labels.append(i[0:4])
    return deleted_labels


def remove_data_from(data_list):
    deleted_data = []
    for i in data_list:
        deleted_data.append(i[4])
    return deleted_data


def choose_best_match(neighbors):
    matches = {}
    for i in neighbors:
        if i in matches:
            matches[i] += 1
        else:
            matches[i] = 1
    label = max(matches.items(), key=operator.itemgetter(1))[0]
    return label


def take2nd(e):
    return e[1]
