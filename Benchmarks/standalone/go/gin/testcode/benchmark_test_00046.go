// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00046(c *gin.Context) {
	var profileBio string
	DB.QueryRow("SELECT bio FROM profiles LIMIT 1").Scan(&profileBio)
	pending := strings.Split(profileBio, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.#~\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	os.Remove("/var/app/data/" + processed)
	c.JSON(200, gin.H{"code": "OK"})
}
