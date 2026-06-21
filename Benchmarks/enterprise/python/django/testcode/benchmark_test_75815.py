# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75815(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    eval(str(data))
    return JsonResponse({"saved": True})
