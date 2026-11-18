# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def apply_redaction(request):
    transcript = json.loads(request.body or b'{}').get("documents_payload", "")
    try:
        _coerced = int(transcript)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    addendum = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(addendum))
    return JsonResponse({"saved": True})
