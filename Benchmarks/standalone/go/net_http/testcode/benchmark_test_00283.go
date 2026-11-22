// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
)

func BenchmarkTest00283(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	var data string
	if len(headerValue) > 0 {
		data = headerValue
	} else {
		data = "default"
	}
	upstreams := map[string]*url.URL{
		"billing": {Scheme: "https", Host: "billing.svc.cluster"},
		"reports": {Scheme: "https", Host: "reports.svc.cluster"},
	}
	upstream := upstreams[data]
	upstreamHost := upstream.Host
	RespondJSON(w, http.StatusOK, map[string]string{"upstream": upstreamHost})
}
