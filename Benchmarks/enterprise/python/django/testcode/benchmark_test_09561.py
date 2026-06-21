# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest09561(request):
    upload_name = request.FILES['upload'].name
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', upload_name):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = upload_name
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
