# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import re


@csrf_exempt
def grant_share(request):
    notice = json.loads(request.body or b'{}').get("workspace_payload", "")
    if not re.fullmatch("^(asc|desc|name|created)$", str(notice)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    wording = notice
    return HttpResponse(mark_safe('<div>' + str(wording) + '</div>'))
