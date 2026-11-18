// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"os/exec"
	"regexp"
)

func BenchmarkTest00048(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.%\\-]+$")
	if !validPattern.MatchString(jsonValue) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := jsonValue
	cmd := exec.Command("python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
