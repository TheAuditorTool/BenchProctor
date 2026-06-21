# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79600(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
