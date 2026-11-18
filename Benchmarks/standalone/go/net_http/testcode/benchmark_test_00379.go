// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os/exec"
)

func BenchmarkTest00379(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := fmt.Sprintf("%s", refererValue)
	cmd := exec.Command("echo", data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
