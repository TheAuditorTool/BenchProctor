# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest05901(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    processed = data[:64]
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return JsonResponse({"saved": True})
