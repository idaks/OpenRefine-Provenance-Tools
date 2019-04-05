import copy
from pprint import pprint

import time

import OpenRefineOperations as OR


def prompt_int(message, min=None, max=None):
    while True:
        input_str = raw_input(message)

        try:
            value = int(input_str)

            if min is not None and value < min:
                raise ValueError
            if max is not None and value > max:
                raise ValueError

        except ValueError:
            pass
        else:
            return value


def prompt_options(options):
    for idx, option in enumerate(options, start=1):
        print(idx, option)

    if not options:
        return 0
    else:
        return prompt_int('Please enter your choice: ', min=1, max=len(options))

# store the complete operation history
def OH_list(history_list):
    past_list= [p for p in history_list['past']]
    future_list=[f for f in history_list['future']]
    complete_list=past_list+future_list
    return complete_list


def OH_id_list(history_list):
    past_id_list=[p['id'] for p in history_list['past']]
    future_id_list=[f['id'] for f in history_list['future']]
    complete_id_list=past_id_list+future_id_list
    return complete_id_list

# previous history list
history_list0=OR.list_history(1981993338999)
pprint(history_list0)
complete_id_list0=OH_id_list(history_list0)

# generate a copy of the operation list storing all of the manipulations
# avoid the breaking caused by override
complete_list0=OH_list(history_list0)
copy_complete_list=copy.deepcopy(complete_list0)

# example: undo to second position
user_=prompt_options(complete_id_list0)
user_choice=complete_id_list0[int(user_)-1]

# undo steps
OR.undo_redo(1981993338999,user_choice)
copy_complete_list.append({u'undo-redo':user_choice})
pprint(OR.list_history(1981993338999))
OR.text_transform(1981993338999,'Customer ID No','value.toNumber()')

# new step can be got from the end of the ['past']
history_list1=OR.list_history(1981993338999)

complete_list1=OH_list(history_list1)
copy_complete_list.append(complete_list1[len(complete_list1)-1])

'''
print the complete records of the manipulations
'''
pprint(copy_complete_list)








