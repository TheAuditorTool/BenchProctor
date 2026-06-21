# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest78012(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = normalise_input(multipart_value)
    return HttpResponse(str(data), content_type='text/html')
