// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"os/exec"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00534(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	data := func(v string) string { return strings.TrimSpace(v) }(rawBody)
	allowedBins := map[string]bool{"ls": true, "cat": true, "date": true, "whoami": true}
	if !allowedBins[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	allowedBin := data
	cmd := exec.Command("python3", "-c", allowedBin)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
