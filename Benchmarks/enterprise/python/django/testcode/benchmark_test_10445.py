# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10445(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
