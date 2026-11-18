// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00545(c *gin.Context) {
	fieldValue := c.PostForm("field")
	os.WriteFile("/var/app/data/"+fieldValue, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
