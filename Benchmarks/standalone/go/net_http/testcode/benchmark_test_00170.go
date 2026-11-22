// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"net/http"
	"net/url"
)

func BenchmarkTest00170(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	decodedBytes, _ := base64.StdEncoding.DecodeString(authHeader)
	data := string(decodedBytes)
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
