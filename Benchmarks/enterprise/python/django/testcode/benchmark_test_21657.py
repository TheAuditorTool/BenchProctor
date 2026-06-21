# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21657(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
