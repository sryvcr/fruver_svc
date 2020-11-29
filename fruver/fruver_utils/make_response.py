def make_response(status: int, data: dict | list) -> dict:
    response = {
        'status': status,
        'data': data,
    }
    return response