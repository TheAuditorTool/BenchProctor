# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import json
import re


@csrf_exempt
def index_metadata(request):
    heading = json.loads(request.body or b'{}').get("media_payload", "")
    if not re.fullmatch("^(asc|desc|name|created)$", str(heading)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    montage = heading
    with open('/var/app/data/' + str(montage), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
