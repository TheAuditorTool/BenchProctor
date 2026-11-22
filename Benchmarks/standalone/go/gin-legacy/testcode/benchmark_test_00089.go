// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"os/exec"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00089(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(authHeader)
	allowedBins := map[string]bool{"ls": true, "cat": true, "date": true, "whoami": true}
	if !allowedBins[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	allowedBin := data
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", allowedBin)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
