// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
)

func BenchmarkTest00251(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	upstreamReq, err := http.NewRequest(http.MethodGet, refererValue, nil)
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
