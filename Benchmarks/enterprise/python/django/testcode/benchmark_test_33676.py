# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33676(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
