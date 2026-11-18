// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os/exec"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00039(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := fmt.Sprintf("%s", refererValue)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	cmd := exec.Command("python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
