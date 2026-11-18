// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00275(c *gin.Context) {
	userID := c.Query("id")
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: userID, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
