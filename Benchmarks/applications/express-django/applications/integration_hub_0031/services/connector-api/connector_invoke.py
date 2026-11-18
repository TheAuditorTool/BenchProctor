# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def invoke_connector(request):
    passage = json.loads(request.body or b'{}').get("integrations_payload", "")
    if passage not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    paragraph = passage
    subprocess.run('echo ' + str(paragraph), shell=True)
    return JsonResponse({"saved": True})
