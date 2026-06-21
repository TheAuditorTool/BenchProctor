# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest38200(request):
    multipart_value = request.POST.get('multipart_field', '')
    entries = os.listdir(str(multipart_value))
    return JsonResponse({'listing': entries}, status=200)
