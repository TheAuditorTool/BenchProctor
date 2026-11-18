// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00477(c *gin.Context) {
	userID := c.Query("id")
	var data string
	for _, token := range strings.Split(userID, ",") {
		data = token
	}
	os.Remove("/var/app/data/" + data)
	c.JSON(200, gin.H{"code": "OK"})
}
