# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest57476(request):
    user_id = request.GET.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', user_id):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = user_id
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
