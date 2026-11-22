# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def run_conversion(request):
    synopsis = json.loads(request.body or b'{}').get("documents_payload", "")
    if synopsis not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    dossier = synopsis
    os.system('echo ' + str(dossier))
    return JsonResponse({"saved": True})
