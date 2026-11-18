// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00212(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	data := func(v string) string { return strings.TrimSpace(v) }(rawBody)
	allowedBins := map[string]bool{"ls": true, "cat": true, "date": true, "whoami": true}
	if !allowedBins[data] {
		http.Error(w, "forbidden", http.StatusForbidden)
		return
	}
	allowedBin := data
	cmd := exec.Command("python3", "-c", allowedBin)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
