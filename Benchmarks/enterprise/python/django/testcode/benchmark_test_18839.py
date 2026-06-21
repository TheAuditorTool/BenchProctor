# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18839(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
