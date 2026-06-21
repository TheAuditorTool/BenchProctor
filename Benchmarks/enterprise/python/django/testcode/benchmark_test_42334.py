# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest42334(request):
    upload_name = request.FILES['upload'].name
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(upload_name)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = upload_name
    eval(str(processed))
    return JsonResponse({"saved": True})
