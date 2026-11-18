// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os/exec"
	"regexp"
)

func BenchmarkTest00052(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := fmt.Sprintf("%s", refererValue)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	cmd := exec.Command("python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
