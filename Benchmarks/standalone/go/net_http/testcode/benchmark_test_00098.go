// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"net/url"
	"regexp"
)

func BenchmarkTest00098(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	hexBytes, _ := hex.DecodeString(userID)
	data := string(hexBytes)
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		http.Error(w, "forbidden host", http.StatusForbidden)
		return
	}
	targetUrl := data
	http.Redirect(w, r, targetUrl, http.StatusFound)
}
