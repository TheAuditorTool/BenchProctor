// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"os/exec"
	"regexp"
)

func BenchmarkTest00541(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	data, _ := url.QueryUnescape(userID)
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
