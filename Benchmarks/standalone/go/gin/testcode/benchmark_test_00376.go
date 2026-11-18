// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00376(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	data := fmt.Sprintf("%s", authHeader)
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
