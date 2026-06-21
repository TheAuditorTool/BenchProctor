# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest52834(request):
    multipart_value = request.POST.get('multipart_field', '')
    os.system('echo ' + str(multipart_value))
    return JsonResponse({"saved": True})
