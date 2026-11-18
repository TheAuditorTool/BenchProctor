# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json


def BenchmarkTest00232(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
