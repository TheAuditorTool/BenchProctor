// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00156(c *gin.Context) {
	hostValue := c.Request.Host
	segments := strings.Split(hostValue, ",")
	data := strings.Join(segments, " ")
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
