// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"net/url"
	"regexp"
	"strings"
)

func BenchmarkTest00442(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	relayPrefix := ""
	if len(headerValue) > 0 {
		relayPrefix = strings.ToLower(headerValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = headerValue
	case "f":
		data = headerValue
	default:
		data = headerValue
	}
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		http.Error(w, "forbidden host", http.StatusForbidden)
		return
	}
	targetUrl := data
	resp, err := http.Get(targetUrl)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	w.Write(body)
}
