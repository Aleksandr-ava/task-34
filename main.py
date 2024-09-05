import inspect


def introspection_info(obj):
    print({'type': type(obj), 'attributes': dir(obj)[5:63]})
    function_module = inspect.getmodule(introspection_info)
    print('module', type(function_module), function_module)
    print('methods', inspect.getmembers(introspection_info))
    return obj


number_info = introspection_info
print(number_info(42))
