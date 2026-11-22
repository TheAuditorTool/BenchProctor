// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
)

func BenchmarkTest00061(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	var data string
	if cookieValue != "" {
		data = cookieValue
	}
	upstreamReq, err := http.NewRequest(http.MethodGet, data, nil)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	upstreamReq.Header.Set("Accept", "application/json")
	resp, err := http.DefaultClient.Do(upstreamReq)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadGateway)
		return
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	w.Write(body)
}
