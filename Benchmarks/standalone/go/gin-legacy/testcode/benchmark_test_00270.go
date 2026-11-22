// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00270(c *gin.Context) {
	userID := c.Query("id")
	var data string
	if userID != "" {
		data = userID
	}
	ioutil.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
