# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest66671(request):
    multipart_value = request.POST.get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(multipart_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = multipart_value
    eval(str(processed))
    return JsonResponse({"saved": True})
