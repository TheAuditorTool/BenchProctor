// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"io"
	"net/http"
	"os/exec"
)

func BenchmarkTest00090(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	data := string(bytes.TrimSpace([]byte(rawBody)))
	cmd := exec.Command("python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
