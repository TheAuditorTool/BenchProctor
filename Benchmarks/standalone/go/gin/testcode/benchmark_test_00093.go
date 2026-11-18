// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00093(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	hexBytes, _ := hex.DecodeString(cookieValue)
	data := string(hexBytes)
	c.Set("data", data)
}
