# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07226(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
