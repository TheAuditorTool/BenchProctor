// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"io"
	"net/http"
	"os/exec"
	"regexp"

	"github.com/gin-gonic/gin"
	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00486(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	data := string(bytes.TrimSpace([]byte(rawBody)))
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.%\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(data, "schema"); err != nil {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	cmd := exec.Command("python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
