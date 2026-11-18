// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00344(c *gin.Context) {
	fieldValue := c.PostForm("field")
	data := strings.ReplaceAll(fieldValue, "\x00", "")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	cmd := exec.Command("python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
