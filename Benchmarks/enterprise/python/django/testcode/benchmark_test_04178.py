# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04178(request):
    upload_name = request.FILES['upload'].name
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(upload_name)})
