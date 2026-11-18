# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def enrich_threshold(request):
    notice = request.GET.get('id', '')
    rendition, _sep, _rest = str(notice).partition('\x00')
    os.system('echo ' + str(rendition))
    return JsonResponse({"saved": True})
