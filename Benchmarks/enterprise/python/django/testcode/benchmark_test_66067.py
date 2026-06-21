# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66067(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
