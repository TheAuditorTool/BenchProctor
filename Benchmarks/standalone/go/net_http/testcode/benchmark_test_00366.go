// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00366(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	segments := strings.Split(uaValue, ",")
	data := strings.Join(segments, " ")
	cmd := exec.Command("sh", "-c", "echo "+data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
