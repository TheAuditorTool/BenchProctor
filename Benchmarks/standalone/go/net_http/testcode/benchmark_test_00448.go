// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"regexp"
	"strings"
)

func BenchmarkTest00448(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	segments := strings.Split(refererValue, ",")
	data := strings.Join(segments, " ")
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.%\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	cmd := exec.Command("sh", "-c", "echo "+processed)
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(output)
}
