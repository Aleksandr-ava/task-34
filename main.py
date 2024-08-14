import inspect


def introspection_info(obj):
    return obj


class Intros:
    def __init__(self):
        self.nomer = 345


nomer_info = Intros()
number_info = introspection_info


class Info_:
    def __init__(self):
        self.info = []

    def type_(self, name):
        self.info.append({'type': type(name)})

    def dir_(self, name):
        self.info.append({'attributes': dir(name)})


info_ = Info_()
print(number_info(42))
function_module = inspect.getmodule(introspection_info)
print('module', type(function_module), function_module)
info_.type_(number_info)
info_.type_(introspection_info)
info_.type_(nomer_info)
print(nomer_info.nomer)
methods_ = inspect.getmembers(Intros, predicate=inspect.isfunction)
print('methods', methods_)
function_module = inspect.getmodule(Intros)
print('module', type(function_module), function_module)
info_.dir_(number_info)
info_.dir_(introspection_info)
info_.dir_(nomer_info)
out = str(list(info_.info))
out = out.replace("[", "")
out = out.replace("]", "")
print(out)
