// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00577(c *gin.Context) {
	pathValue := c.Param("id")
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: pathValue, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
