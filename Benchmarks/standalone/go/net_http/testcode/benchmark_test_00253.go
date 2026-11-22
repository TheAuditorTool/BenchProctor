// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"net/url"
	"os/exec"
	"time"
)

func BenchmarkTest00253(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	data, _ := url.QueryUnescape(userID)
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
