# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42272(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
