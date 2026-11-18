# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def push_syndication(request):
    excerpt = json.loads(request.body or b'{}').get("publishing_payload", "")
    subprocess.run('echo ' + str(excerpt), shell=True)
    return JsonResponse({"saved": True})
