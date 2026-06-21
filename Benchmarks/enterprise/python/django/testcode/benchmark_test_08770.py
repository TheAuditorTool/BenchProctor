# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08770(request):
    upload_name = request.FILES['upload'].name
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(upload_name)})
