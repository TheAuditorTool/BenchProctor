# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20918(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
