# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest51021(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
