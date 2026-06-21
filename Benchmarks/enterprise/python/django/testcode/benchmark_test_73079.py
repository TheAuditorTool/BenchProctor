# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73079(request):
    multipart_value = request.POST.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
