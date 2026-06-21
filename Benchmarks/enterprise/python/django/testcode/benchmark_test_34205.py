# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34205(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
