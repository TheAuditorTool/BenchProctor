// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"net/url"
	"regexp"
)

func BenchmarkTest00182(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(originValue)
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
