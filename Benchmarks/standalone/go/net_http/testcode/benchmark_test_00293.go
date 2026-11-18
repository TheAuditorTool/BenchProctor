// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00293(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	capture := func() string { return strings.TrimSpace(refererValue) }
	data := capture()
	resp, err := http.Get(data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	w.Write(body)
}
