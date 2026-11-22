// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"os/exec"
	"time"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00037(c *gin.Context) {
	userID := c.Query("id")
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", userID)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
