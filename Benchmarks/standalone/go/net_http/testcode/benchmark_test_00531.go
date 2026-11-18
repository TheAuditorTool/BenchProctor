// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00531(w http.ResponseWriter, r *http.Request) {
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
	resp, err := http.Get(data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	w.Write(body)
}
