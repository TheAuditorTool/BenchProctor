// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00005(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	xmlBody := string(rawBytes)
	var data string
	if xmlBody != "" {
		data = xmlBody
	}
	c.Set("data", data)
}
