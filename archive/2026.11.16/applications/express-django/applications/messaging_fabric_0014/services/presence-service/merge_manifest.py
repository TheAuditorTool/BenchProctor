# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def merge_manifest(request):
    summary = request.COOKIES.get('session_token', '')
    bulletin = summary if summary else 'default'
    os.system('echo ' + str(bulletin))
    return JsonResponse({"saved": True})
