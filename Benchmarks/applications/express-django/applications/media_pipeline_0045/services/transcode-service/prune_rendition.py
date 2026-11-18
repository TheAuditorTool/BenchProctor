# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def prune_rendition(request):
    notice = json.loads(request.body or b'{}').get('payload', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(notice)
    subprocess.run(['echo', rendition], shell=False)
    return JsonResponse({"saved": True})
