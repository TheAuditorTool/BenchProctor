// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00157(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var data string
	if len(authHeader) > 0 {
		data = authHeader
	} else {
		data = "default"
	}
	cmd := exec.Command("echo", data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/plain", output)
}
