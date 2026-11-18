# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from marshmallow import Schema, fields, validate, ValidationError


def BenchmarkTest00287(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.%\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
