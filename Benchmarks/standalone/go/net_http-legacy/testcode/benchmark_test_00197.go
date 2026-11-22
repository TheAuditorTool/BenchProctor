// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/json"
	"net/http"
	"os/exec"
	"regexp"
	"time"
)

func BenchmarkTest00197(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(jsonValue) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := jsonValue
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
