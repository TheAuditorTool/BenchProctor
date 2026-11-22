// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"net/url"
	"regexp"
	"strings"
)

func BenchmarkTest00014(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", originValue)
	data := relayBuilder.String()
	parsedURL, parseErr := url.Parse(data)
	if parseErr != nil || (parsedURL.Scheme != "http" && parsedURL.Scheme != "https") || parsedURL.User != nil || strings.ContainsAny(data, "\\ \t\r\n") || !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		http.Error(w, "forbidden host", http.StatusForbidden)
		return
	}
	targetUrl := data
	w.Header().Set("Location", targetUrl)
	w.WriteHeader(http.StatusSeeOther)
}
