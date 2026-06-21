# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01179(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
