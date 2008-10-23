from djangologging import SUPPRESS_OUTPUT_ATTR


def supress_logging_output(func=None):
    """
    Decorates a view to prevent any log messages generated by it (or anything 
    it calls) from being outputted to the browser.
    """  
    def decorated(*args, **kwargs):
        response = func(*args, **kwargs)
        setattr(response, SUPPRESS_OUTPUT_ATTR, True)
        return response
    return decorated