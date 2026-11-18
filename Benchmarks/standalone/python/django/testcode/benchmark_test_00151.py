# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach


def BenchmarkTest00151(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = bleach.clean(markdown.markdown(data))
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
