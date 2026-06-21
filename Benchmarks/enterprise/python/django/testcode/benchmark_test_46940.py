# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest46940(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
