// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"os/exec"
	"strings"
	"time"
)

func BenchmarkTest00016(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	authHeader := r.Header.Get("Authorization")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(authHeader)
	allowedBins := map[string]bool{"ls": true, "cat": true, "date": true, "whoami": true}
	if !allowedBins[data] {
		http.Error(w, "forbidden", http.StatusForbidden)
		return
	}
	allowedBin := data
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", allowedBin)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
