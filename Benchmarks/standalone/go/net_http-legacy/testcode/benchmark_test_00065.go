// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"net/url"
	"strings"
)

func BenchmarkTest00065(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	hostValue := r.Host
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", hostValue)
	data := relayBuilder.String()
	upstreams := map[string]*url.URL{
		"billing": {Scheme: "https", Host: "billing.svc.cluster"},
		"reports": {Scheme: "https", Host: "reports.svc.cluster"},
	}
	upstream := upstreams[data]
	upstreamHost := upstream.Host
	RespondJSON(w, http.StatusOK, map[string]string{"upstream": upstreamHost})
}
