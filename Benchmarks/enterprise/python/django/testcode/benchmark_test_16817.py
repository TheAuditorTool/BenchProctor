# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach


def BenchmarkTest16817(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    processed = bleach.clean(markdown.markdown(data))
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
