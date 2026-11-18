# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00610(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
