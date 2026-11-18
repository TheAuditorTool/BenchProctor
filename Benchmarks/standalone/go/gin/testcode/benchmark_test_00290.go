// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00290(c *gin.Context) {
	fieldValue := c.PostForm("field")
	data, _ := url.QueryUnescape(fieldValue)
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
