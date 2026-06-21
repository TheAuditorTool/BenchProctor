# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52510(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
