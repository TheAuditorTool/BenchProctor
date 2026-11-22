// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"os/exec"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00002(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(headerValue)
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
