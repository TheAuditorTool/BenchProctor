# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35223(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
