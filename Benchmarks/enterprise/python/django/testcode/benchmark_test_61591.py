# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61591(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
