# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00186(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
