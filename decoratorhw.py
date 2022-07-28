def decor(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)

    return wrapper


@decor
def div(x, y, z):
    res = x - y - z
    return res


# div = decor(div)  #1-4-5=-8     5-4-1=0
div(1, 4, 5)