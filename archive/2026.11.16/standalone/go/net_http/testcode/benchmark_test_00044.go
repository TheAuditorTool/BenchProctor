// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"net/http"
	"os/exec"
)

func BenchmarkTest00044(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	decodedBytes, _ := base64.StdEncoding.DecodeString(cookieValue)
	data := string(decodedBytes)
	cmd := exec.Command("sh", "-c", "echo "+data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
