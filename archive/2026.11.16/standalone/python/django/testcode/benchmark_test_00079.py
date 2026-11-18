# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jsonschema


def BenchmarkTest00079(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = (lambda v: v.strip())(ua_value)
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
