# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00562(request):
    field_value = request.POST.get('field', '')
    exec(str(field_value))
    return JsonResponse({"saved": True})
