# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00654(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
