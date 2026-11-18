// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os/exec"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00548(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := fmt.Sprintf("%s", refererValue)
	cmd := exec.Command("echo", data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/plain", output)
}
