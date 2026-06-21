# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20982(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
