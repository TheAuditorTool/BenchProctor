// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00143(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	data := strings.ReplaceAll(headerValue, "\x00", "")
	cmd := exec.Command("python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
