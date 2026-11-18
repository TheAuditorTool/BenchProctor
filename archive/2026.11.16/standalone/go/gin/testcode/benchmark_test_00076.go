// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00076(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	data := func(v string) string { return strings.TrimSpace(v) }(rawBody)
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
