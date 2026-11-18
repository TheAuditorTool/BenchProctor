// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"io"
	"net/http"
	"os/exec"
	"regexp"

	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00178(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	data := string(bytes.TrimSpace([]byte(rawBody)))
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
