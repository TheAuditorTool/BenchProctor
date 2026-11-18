// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"net/http"
	"os/exec"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00067(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	decodedBytes, _ := base64.StdEncoding.DecodeString(cookieValue)
	data := string(decodedBytes)
	cmd := exec.Command("sh", "-c", "echo "+data)
	output, err := cmd.CombinedOutput()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/plain", output)
}
