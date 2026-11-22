// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/url"
	"os/exec"
	"time"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00285(c *gin.Context) {
	userID := c.Query("id")
	data, _ := url.QueryUnescape(userID)
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
