# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def edit_document(request):
    excerpt = json.loads(request.body or b'{}').get("workspace_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", excerpt):
        return JsonResponse({'error': 'forbidden'}, status=400)
    notice = excerpt
    os.unlink('/var/app/data/' + str(notice))
    return JsonResponse({"saved": True})
