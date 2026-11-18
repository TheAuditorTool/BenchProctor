// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00497(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(uaValue)
	cmd := exec.Command("echo", data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
