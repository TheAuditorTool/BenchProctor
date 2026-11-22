// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"os/exec"
)

func BenchmarkTest00150(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	hexBytes, _ := hex.DecodeString(userID)
	data := string(hexBytes)
	cmd := exec.Command("sh", "-c", "echo "+data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
