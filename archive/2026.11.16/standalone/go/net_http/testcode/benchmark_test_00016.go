// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
)

func BenchmarkTest00016(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(refererValue)
	cmd := exec.Command("sh", "-c", "echo "+data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
