// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/hex"
	"net/http"
	"os/exec"
	"time"
)

func BenchmarkTest00052(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	hexBytes, _ := hex.DecodeString(cookieValue)
	data := string(hexBytes)
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
