// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00091(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	form := submissionForm{payload: rawBody}
	data := form.payload
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
