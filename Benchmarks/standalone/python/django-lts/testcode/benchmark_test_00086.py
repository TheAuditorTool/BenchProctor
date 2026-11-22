# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach
import json


def BenchmarkTest00086(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    processed = bleach.clean(markdown.markdown(data))
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
