// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"regexp"
	"strings"
)

func BenchmarkTest00305(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := strings.Join(strings.FieldsFunc(refererValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		http.Error(w, "forbidden host", http.StatusForbidden)
		return
	}
	targetUrl := data
	http.Redirect(w, r, targetUrl, http.StatusFound)
}
