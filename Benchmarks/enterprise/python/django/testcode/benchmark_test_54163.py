# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54163(request):
    multipart_value = request.POST.get('multipart_field', '')
    request.session['data'] = str(multipart_value)
    return JsonResponse({"saved": True})
