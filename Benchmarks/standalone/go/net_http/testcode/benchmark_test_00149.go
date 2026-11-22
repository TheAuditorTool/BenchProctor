// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"os/exec"
	"regexp"
	"strings"
	"time"
)

func BenchmarkTest00149(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := func(v string) string { return strings.TrimSpace(v) }(refererValue)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
