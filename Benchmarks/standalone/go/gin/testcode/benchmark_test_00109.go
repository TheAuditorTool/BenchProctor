// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os/exec"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00109(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", authHeader)
	data := relayBuilder.String()
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	cmd := exec.Command("sh", "-c", "echo "+processed)
	output, err := cmd.CombinedOutput()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/plain", output)
}
