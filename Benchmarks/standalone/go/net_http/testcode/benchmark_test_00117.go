// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"os/exec"
)

func BenchmarkTest00117(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	var data string
	if len(jsonValue) > 0 {
		data = jsonValue
	} else {
		data = "default"
	}
	cmd := exec.Command("python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
