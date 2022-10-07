from .cart import Cart


def cart(request):
    """
    An instance of Cart class sent to all views
    And we will have access to it in all templates.
    """
    return {'cart': Cart(request)}
