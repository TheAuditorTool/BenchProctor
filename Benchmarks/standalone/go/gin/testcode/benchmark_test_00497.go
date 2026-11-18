// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00497(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	var data string
	if len(refererValue) > 0 {
		data = refererValue
	} else {
		data = "default"
	}
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
