// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00210(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	hexBytes, _ := hex.DecodeString(headerValue)
	data := string(hexBytes)
	c.Redirect(http.StatusFound, data)
}
