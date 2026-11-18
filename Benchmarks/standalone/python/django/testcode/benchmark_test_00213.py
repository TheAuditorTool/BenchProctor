# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00213(request):
    field_value = request.POST.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
