# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import urllib.request
import urllib.parse
import ssl


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest71825(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = default_blank(multipart_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
