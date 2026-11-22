// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00275(c *gin.Context) {
	header, err := c.FormFile("upload")
	if err != nil {
		c.String(http.StatusBadRequest, "bad upload")
		return
	}
	uploadName := header.Filename
	var data string
	if len(uploadName) > 0 {
		data = uploadName
	} else {
		data = "default"
	}
	redisClient.HSet(context.Background(), "session:"+c.GetString("user"), map[string]interface{}{"display_name": data, "locale": "en"})
	c.JSON(200, gin.H{"code": "OK"})
}
