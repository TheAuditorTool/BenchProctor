# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from pathlib import Path


@csrf_exempt
def audit_digest(request):
    remark = request.body.decode('utf-8')
    persona = remark if remark else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    notice = persona
    Path('/var/app/data/' + str(notice)).write_text('data')
    return JsonResponse({"saved": True})
