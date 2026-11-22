# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import jsonschema


def BenchmarkTest00113(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
