// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00115(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	data := strings.ReplaceAll(dbValue, "\x00", "")
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.#%\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
