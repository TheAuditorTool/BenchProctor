// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"regexp"
)

func BenchmarkTest00040(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.%\\-]+$")
	if !validPattern.MatchString(uaValue) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := uaValue
	cmd := exec.Command("sh", "-c", "echo "+processed)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
