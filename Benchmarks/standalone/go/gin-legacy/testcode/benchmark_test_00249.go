// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00249(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	data := originValue
	if _, after, ok := strings.Cut(originValue, ","); ok {
		data = after
	}
	ioutil.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
