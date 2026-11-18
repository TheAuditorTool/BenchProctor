// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00556(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(cookieValue)
	cmd := exec.Command("python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
