// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"regexp"
	"strings"
)

func BenchmarkTest00452(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	data := strings.ReplaceAll(fieldValue, "\x00", "")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	cmd := exec.Command("python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
