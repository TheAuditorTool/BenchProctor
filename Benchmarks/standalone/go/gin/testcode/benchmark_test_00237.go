// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00237(c *gin.Context) {
	fieldValue := c.PostForm("field")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(fieldValue)
	cmd := exec.Command("echo", data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/plain", output)
}
