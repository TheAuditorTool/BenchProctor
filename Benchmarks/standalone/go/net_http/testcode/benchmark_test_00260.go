// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"os/exec"
	"time"
)

func BenchmarkTest00260(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", userID)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
