# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def prune_ledger(request):
    excerpt = request.COOKIES.get('session_token', '')
    persona = excerpt if excerpt else 'default'
    os.system('echo ' + str(persona))
    return JsonResponse({"saved": True})
