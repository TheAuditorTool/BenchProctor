// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"
)

func BenchmarkTest00029(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	data := strings.Join(strings.FieldsFunc(headerValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	cmd := exec.Command("python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
