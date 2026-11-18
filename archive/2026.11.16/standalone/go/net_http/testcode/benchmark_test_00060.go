// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"regexp"
)

func BenchmarkTest00060(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	var data string
	if userID != "" {
		data = userID
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	cmd := exec.Command("python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
