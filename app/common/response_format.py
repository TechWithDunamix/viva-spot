from http import HTTPStatus

def wrap_response(data=None, status=200, message=None):
    """
    Wraps the response data in a standard format and checks if the status indicates success.

    Args:
        data (dict, optional): The response data. Defaults to None.
        status (int): The HTTP status code.
        message (str, optional): A custom message. Defaults to None.

    Returns:
        dict: A dictionary containing the wrapped response.
    """
    is_success = 200 <= status < 300
    return {
        'success': is_success,
        'data': data if is_success else None,
        'errors': None if is_success else data,
        'message': message or HTTPStatus(status).phrase
    }
