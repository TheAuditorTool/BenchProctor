# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66994(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
