# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35615(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
