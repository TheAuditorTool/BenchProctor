// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00401(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(cookieValue)
	cmd := exec.Command("python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
