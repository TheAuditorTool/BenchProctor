// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00209(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(rawBody)
	allowedBins := map[string]bool{"ls": true, "cat": true, "date": true, "whoami": true}
	if !allowedBins[data] {
		http.Error(w, "forbidden", http.StatusForbidden)
		return
	}
	allowedBin := data
	cmd := exec.Command("echo", allowedBin)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
