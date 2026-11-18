// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00096(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(headerValue)
	cmd := exec.Command("python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
