# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26586(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    eval(str(data))
    return JsonResponse({"saved": True})
