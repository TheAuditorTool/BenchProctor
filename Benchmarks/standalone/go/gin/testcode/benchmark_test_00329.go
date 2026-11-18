// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00329(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	hexBytes, _ := hex.DecodeString(authHeader)
	data := string(hexBytes)
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
