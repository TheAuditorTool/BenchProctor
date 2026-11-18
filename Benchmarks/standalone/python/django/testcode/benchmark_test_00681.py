# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse


def BenchmarkTest00681(request):
    multipart_value = request.POST.get('multipart_field', '')
    kind = 'json' if str(multipart_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(multipart_value).strip()
        case _:
            data = str(multipart_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
