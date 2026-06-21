# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01491(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
