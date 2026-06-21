# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49019(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
