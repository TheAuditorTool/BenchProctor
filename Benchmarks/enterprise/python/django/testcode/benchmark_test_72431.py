# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest72431(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    auth_check('user', data)
    return JsonResponse({"saved": True})
