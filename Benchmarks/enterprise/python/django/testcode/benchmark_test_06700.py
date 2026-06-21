# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06700(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
