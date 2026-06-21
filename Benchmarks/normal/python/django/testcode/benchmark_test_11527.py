# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11527(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    eval(str(data))
    return JsonResponse({"saved": True})
