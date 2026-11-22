// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"fmt"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/yuin/goldmark"
)

func BenchmarkTest00097(c *gin.Context) {
	userID := c.Query("id")
	data := strings.ReplaceAll(userID, "\x00", "")
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	c.Header("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(c.Writer, "<p>Results for %s</p>", processed)
}
