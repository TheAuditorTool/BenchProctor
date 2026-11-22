// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00162(c *gin.Context) {
	rawBytes, err := ioutil.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	xmlBody := string(rawBytes)
	c.Writer.Header().Add("Set-Cookie", "session=" + url.QueryEscape(xmlBody) + "; Path=/; Secure; HttpOnly; SameSite=Strict")
	c.JSON(200, gin.H{"code": "OK"})
}
