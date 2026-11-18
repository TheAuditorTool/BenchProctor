// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00162(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	segments := strings.Split(userID, ",")
	data := strings.Join(segments, " ")
	cmd := exec.Command("sh", "-c", "echo "+data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
