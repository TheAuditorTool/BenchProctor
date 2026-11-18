// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00544(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	data := func(v string) string { return strings.TrimSpace(v) }(rawBody)
	cmd := exec.Command("sh", "-c", "echo "+data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
