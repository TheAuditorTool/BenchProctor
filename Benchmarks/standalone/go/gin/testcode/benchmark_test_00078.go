// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00078(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	form := submissionForm{payload: uaValue}
	data := form.payload
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
