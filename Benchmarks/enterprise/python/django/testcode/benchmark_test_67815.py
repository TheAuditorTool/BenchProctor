# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67815(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
