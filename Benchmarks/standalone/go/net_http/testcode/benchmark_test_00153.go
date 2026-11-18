// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00153(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	capture := func() string { return strings.TrimSpace(refererValue) }
	data := capture()
	cmd := exec.Command("sh", "-c", "echo "+data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
