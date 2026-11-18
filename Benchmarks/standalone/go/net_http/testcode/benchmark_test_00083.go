// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"regexp"
)

func BenchmarkTest00083(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	var data string
	if len(userID) > 0 {
		data = userID
	} else {
		data = "default"
	}
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		http.Error(w, "forbidden host", http.StatusForbidden)
		return
	}
	targetUrl := data
	http.Redirect(w, r, targetUrl, http.StatusFound)
}
