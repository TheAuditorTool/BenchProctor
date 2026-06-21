# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest28794(request):
    user_id = request.GET.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(user_id)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = user_id
    values = str(processed).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
