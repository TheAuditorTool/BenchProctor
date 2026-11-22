// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io/ioutil"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00189(c *gin.Context) {
	fieldValue := c.PostForm("field")
	data := fmt.Sprintf("%s", fieldValue)
	ioutil.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
