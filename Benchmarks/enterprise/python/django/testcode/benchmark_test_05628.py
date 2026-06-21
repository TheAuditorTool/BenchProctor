# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest05628(request):
    upload_name = request.FILES['upload'].name
    data = normalise_input(upload_name)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
