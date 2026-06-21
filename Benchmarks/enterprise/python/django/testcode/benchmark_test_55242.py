# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest55242(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = normalise_input(multipart_value)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
