# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach


def BenchmarkTest00017(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    processed = bleach.clean(markdown.markdown(data))
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
