# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest31219(request):
    user_id = request.GET.get('id', '')
    data = coalesce_blank(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
