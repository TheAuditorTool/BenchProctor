// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00509(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	hexBytes, _ := hex.DecodeString(authHeader)
	data := string(hexBytes)
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
