// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"net/http"
	"net/url"
	"regexp"
)

func BenchmarkTest00046(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	var data string
	if len(originValue) > 0 {
		data = originValue
	} else {
		data = "default"
	}
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		http.Error(w, "forbidden host", http.StatusForbidden)
		return
	}
	targetUrl := data
	conn, err := net.Dial("tcp", targetUrl)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
