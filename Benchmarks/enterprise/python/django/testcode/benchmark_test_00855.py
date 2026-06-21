# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00855(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
