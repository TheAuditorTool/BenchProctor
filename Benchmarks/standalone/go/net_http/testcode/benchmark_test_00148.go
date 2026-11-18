// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"regexp"
)

func BenchmarkTest00148(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	var data string
	if headerValue != "" {
		data = headerValue
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
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
