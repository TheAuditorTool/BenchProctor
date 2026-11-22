# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json


def BenchmarkTest00232(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    return HttpResponse(mark_safe('<div>' + str(json_value) + '</div>'))
