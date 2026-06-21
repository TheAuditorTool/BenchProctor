# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42172(request):
    multipart_value = request.POST.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
