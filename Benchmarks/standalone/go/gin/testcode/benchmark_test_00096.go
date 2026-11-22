// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"os/exec"
	"regexp"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00096(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := func(v string) string { return strings.TrimSpace(v) }(refererValue)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
