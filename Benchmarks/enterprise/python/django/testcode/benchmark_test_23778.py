# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23778(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
