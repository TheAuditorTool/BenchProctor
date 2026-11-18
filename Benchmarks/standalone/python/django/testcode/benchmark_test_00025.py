# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from marshmallow import Schema, fields, validate, ValidationError


def BenchmarkTest00025(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.%\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
