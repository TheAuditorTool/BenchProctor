// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00286(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.%\\-]+$")
	if !validPattern.MatchString(uaValue) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := uaValue
	cmd := exec.Command("sh", "-c", "echo "+processed)
	output, err := cmd.CombinedOutput()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/plain", output)
}
