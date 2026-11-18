// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00276(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	data := strings.ReplaceAll(rawBody, "\x00", "")
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
