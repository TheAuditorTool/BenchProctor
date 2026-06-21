# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest48405(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
