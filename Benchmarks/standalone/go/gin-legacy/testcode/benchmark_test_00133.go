// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"os/exec"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00133(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", refererValue)
	data := relayBuilder.String()
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
