import test as t
import copy as cp

t.t_list[0].newn('okay')
if cp.deepcopy(t.t_list[1]) in t.t_list:
    print('ooo')
