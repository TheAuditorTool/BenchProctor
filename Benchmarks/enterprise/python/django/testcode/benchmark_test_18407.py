# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest18407(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
