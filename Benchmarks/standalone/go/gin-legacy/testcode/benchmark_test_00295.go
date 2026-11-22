// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00295(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	var data string
	if uaValue != "" {
		data = uaValue
	}
	allowedBins := map[string]bool{"ls": true, "cat": true, "date": true, "whoami": true}
	if !allowedBins[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	allowedBin := data
	cmd := exec.Command("echo", allowedBin)
	output, err := cmd.CombinedOutput()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/plain", output)
}
