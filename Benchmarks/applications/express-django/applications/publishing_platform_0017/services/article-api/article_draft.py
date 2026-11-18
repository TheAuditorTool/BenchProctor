# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def draft_article(request):
    excerpt = json.loads(request.body or b'{}').get("publishing_payload", "")
    with open('/var/app/data/' + str(excerpt), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
