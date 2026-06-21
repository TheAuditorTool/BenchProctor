# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05790(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
