// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00417(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(refererValue)
	cmd := exec.Command("sh", "-c", "echo "+data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
