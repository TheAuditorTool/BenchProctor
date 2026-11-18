// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
)

func BenchmarkTest00430(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	var data string
	if len(authHeader) > 0 {
		data = authHeader
	} else {
		data = "default"
	}
	cmd := exec.Command("echo", data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
