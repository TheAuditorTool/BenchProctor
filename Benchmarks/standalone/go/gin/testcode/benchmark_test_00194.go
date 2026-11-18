// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00194(c *gin.Context) {
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
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
