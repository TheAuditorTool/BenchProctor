# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pathlib import Path
import json


@csrf_exempt
def create_session(request):
    transcript = json.loads(request.body or b'{}').get("identity_payload", "")
    base = Path('/var/app/data').resolve()
    candidate = (base / transcript).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    synopsis = str(candidate)
    with open(synopsis, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
