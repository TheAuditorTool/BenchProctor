# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02410(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
