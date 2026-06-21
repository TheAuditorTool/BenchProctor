# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12249(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
