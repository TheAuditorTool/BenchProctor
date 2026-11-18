// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os/exec"
	"regexp"
	"strings"
)

func BenchmarkTest00105(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", authHeader)
	data := relayBuilder.String()
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
