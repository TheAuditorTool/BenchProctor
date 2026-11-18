// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00258(c *gin.Context) {
	var profileBio string
	DB.QueryRow("SELECT bio FROM profiles LIMIT 1").Scan(&profileBio)
	data := strings.ReplaceAll(profileBio, "\x00", "")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	content, err := os.ReadFile("/var/app/data/" + processed)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
