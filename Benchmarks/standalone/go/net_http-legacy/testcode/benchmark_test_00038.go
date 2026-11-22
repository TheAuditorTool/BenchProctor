// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"strings"
)

func BenchmarkTest00038(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	multipartValue := r.FormValue("multipart_field")
	relayPrefix := ""
	if len(multipartValue) > 0 {
		relayPrefix = strings.ToLower(multipartValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = multipartValue
	case "f":
		data = multipartValue
	default:
		data = multipartValue
	}
	upstreams := map[string]*url.URL{
		"billing": {Scheme: "https", Host: "billing.svc.cluster"},
		"reports": {Scheme: "https", Host: "reports.svc.cluster"},
	}
	upstream := upstreams[data]
	if upstream == nil {
		http.Error(w, "unknown service", http.StatusNotFound)
		return
	}
	upstreamHost := upstream.Host
	RespondJSON(w, http.StatusOK, map[string]string{"upstream": upstreamHost})
}
