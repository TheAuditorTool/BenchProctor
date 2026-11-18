// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00536(c *gin.Context) {
	var profileBio string
	DB.QueryRow("SELECT bio FROM profiles LIMIT 1").Scan(&profileBio)
	var data string
	if profileBio != "" {
		data = profileBio
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	os.Remove("/var/app/data/" + processed)
	c.JSON(200, gin.H{"code": "OK"})
}
