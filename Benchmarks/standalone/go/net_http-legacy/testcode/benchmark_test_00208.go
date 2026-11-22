// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func BenchmarkTest00208(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	refererValue := r.Header.Get("Referer")
	data := fmt.Sprintf("%s", refererValue)
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
	body, _ := ioutil.ReadAll(resp.Body)
	w.Write(body)
}
