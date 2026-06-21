# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach


def BenchmarkTest79986(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    processed = bleach.clean(markdown.markdown(data))
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
