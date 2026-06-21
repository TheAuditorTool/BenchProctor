# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest54052(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = relay_value(multipart_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
