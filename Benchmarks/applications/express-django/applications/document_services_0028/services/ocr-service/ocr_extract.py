# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path
import json


@csrf_exempt
def extract_text(request):
    heading = json.loads(request.body or b'{}').get("documents_payload", "")
    base = Path('/var/app/data').resolve()
    candidate = (base / heading).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    dossier = str(candidate)
    os.unlink(dossier)
    return JsonResponse({"saved": True})
