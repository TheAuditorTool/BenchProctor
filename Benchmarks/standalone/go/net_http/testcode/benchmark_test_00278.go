// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"net/url"
)

func BenchmarkTest00278(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	data := fmt.Sprintf("%s", uaValue)
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
