// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00014(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	content, err := os.ReadFile("/var/app/data/" + dbValue)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
