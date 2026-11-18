// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"os/exec"
	"regexp"
	"strings"

	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00354(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(jsonValue)
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.%\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(data, "schema"); err != nil {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	cmd := exec.Command("python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	w.Write(output)
}
