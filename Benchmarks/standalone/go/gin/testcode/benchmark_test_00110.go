// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00110(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	xmlBody := string(rawBytes)
	data := xmlBody
	if _, after, ok := strings.Cut(xmlBody, ","); ok {
		data = after
	}
	os.Remove("/var/app/data/" + data)
	c.JSON(200, gin.H{"code": "OK"})
}
