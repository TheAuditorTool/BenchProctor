# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13497(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
