// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00246(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	var data string
	if headerValue != "" {
		data = headerValue
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	cmd := exec.Command("sh", "-c", "echo "+processed)
	output, err := cmd.CombinedOutput()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/plain", output)
}
