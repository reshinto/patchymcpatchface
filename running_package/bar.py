import mypackage


def bar_main():
    print(__name__)
    print("Running mypackage.foo.target_function()")
    mypackage.foo.target_function()
