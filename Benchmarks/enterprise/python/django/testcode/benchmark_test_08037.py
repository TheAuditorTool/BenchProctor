# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08037(request):
    multipart_value = request.POST.get('multipart_field', '')
    os.remove(str(multipart_value))
    return JsonResponse({"saved": True})
