# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json


@csrf_exempt
def solve_allocation(request):
    headline = json.loads(request.body or b'{}').get("inventory_payload", "")
    return HttpResponse(mark_safe('<div>' + str(headline) + '</div>'))
