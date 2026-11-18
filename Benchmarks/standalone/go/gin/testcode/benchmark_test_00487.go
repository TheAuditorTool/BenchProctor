// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00487(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	var data string
	for _, token := range strings.Split(dbValue, ",") {
		data = token
	}
	os.Remove("/var/app/data/" + data)
	c.JSON(200, gin.H{"code": "OK"})
}
