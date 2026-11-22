// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00034(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	relayPrefix := ""
	if len(dbValue) > 0 {
		relayPrefix = strings.ToLower(dbValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = dbValue
	case "f":
		data = dbValue
	default:
		data = dbValue
	}
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
