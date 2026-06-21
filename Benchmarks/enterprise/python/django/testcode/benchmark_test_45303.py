# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45303(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
