// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00082(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(refererValue)
	cmd := exec.Command("sh", "-c", "echo "+data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/plain", output)
}
