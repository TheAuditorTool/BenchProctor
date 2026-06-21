# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02690(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
