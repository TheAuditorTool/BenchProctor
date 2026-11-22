# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from django.http import HttpResponse
from django.template import Template, Context
import json


@csrf_exempt
def stream_activity(request):
    note = json.loads(request.body or b'{}').get("workspace_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", note):
        return JsonResponse({'error': 'forbidden'}, status=400)
    transcript = note
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(transcript)}))
    return HttpResponse(page)
