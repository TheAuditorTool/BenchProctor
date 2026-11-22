// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/hex"
	"net/http"
	"os/exec"
	"time"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00004(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	hexBytes, _ := hex.DecodeString(cookieValue)
	data := string(hexBytes)
	allowedBins := map[string]bool{"ls": true, "cat": true, "date": true, "whoami": true}
	if !allowedBins[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	allowedBin := data
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", allowedBin)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
