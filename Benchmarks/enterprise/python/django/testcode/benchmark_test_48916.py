# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48916(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
