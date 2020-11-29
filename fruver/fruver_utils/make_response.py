def make_response(status: int, data: dict):
    response = {
        'status': status,
        'data': data
    }
    return response