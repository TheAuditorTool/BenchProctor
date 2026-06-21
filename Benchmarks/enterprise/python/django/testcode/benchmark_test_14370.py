# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14370(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
