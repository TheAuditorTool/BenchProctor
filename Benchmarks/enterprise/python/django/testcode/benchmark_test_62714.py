# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62714(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
