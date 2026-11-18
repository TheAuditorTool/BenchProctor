// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00106(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: uaValue, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
