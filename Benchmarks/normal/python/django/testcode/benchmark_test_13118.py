# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13118(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
