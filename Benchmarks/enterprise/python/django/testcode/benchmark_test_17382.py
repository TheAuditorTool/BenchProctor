# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17382(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
