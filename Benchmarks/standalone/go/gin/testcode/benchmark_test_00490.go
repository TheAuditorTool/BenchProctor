// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00490(c *gin.Context) {
	var profileBio string
	DB.QueryRow("SELECT bio FROM profiles LIMIT 1").Scan(&profileBio)
	var data string
	if len(profileBio) > 0 {
		data = profileBio
	} else {
		data = "default"
	}
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
