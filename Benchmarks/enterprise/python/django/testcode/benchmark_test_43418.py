# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest43418(request):
    user_id = request.GET.get('id', '')
    data = to_text(user_id)
    auth_check('user', data)
    return JsonResponse({"saved": True})
