// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os/exec"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00493(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(headerValue)
	cmd := exec.Command("python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
