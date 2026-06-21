# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60183(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
