// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"
	"path/filepath"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00266(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var data string
	if commentText != "" {
		data = commentText
	}
	checkedPath := filepath.Join("/var/app/data", filepath.Base(data))
	os.Remove(checkedPath)
	c.JSON(200, gin.H{"code": "OK"})
}
