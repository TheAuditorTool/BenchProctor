# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43230(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
