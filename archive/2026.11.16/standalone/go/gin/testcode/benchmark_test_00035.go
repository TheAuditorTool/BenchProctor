// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os/exec"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00035(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	data := strings.Join(strings.FieldsFunc(headerValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	cmd := exec.Command("python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
