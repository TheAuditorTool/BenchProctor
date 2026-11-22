# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from marshmallow import Schema, fields, validate, ValidationError


def BenchmarkTest00143(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % (header_value,)
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.%\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
