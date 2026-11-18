// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00126(c *gin.Context) {
	var profileBio string
	DB.QueryRow("SELECT bio FROM profiles LIMIT 1").Scan(&profileBio)
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(profileBio)
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
