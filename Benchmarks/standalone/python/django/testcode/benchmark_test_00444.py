# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00444(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ' '.join(parts)
    exec(str(data))
    return JsonResponse({"saved": True})
