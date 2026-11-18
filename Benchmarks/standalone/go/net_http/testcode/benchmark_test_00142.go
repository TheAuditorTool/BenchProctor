// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"net/url"
	"regexp"
	"strings"
)

func BenchmarkTest00142(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	data := strings.Join(strings.FieldsFunc(xmlBody, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		http.Error(w, "forbidden host", http.StatusForbidden)
		return
	}
	targetUrl := data
	http.Redirect(w, r, targetUrl, http.StatusFound)
}
