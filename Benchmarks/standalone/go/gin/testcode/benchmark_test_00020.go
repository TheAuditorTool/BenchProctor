// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net"
	"net/http"
	"net/url"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00020(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	var data string
	if jsonValue != "" {
		data = jsonValue
	}
	parsedURL, _ := url.Parse(data)
	checkedHost := parsedURL.Hostname()
	if resolvedAddrs, lookupErr := net.LookupHost(checkedHost); lookupErr == nil && len(resolvedAddrs) > 0 {
		checkedHost = resolvedAddrs[0]
	}
	if regexp.MustCompile("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").MatchString(checkedHost) {
		c.String(http.StatusForbidden, "private range blocked")
		return
	}
	targetUrl := data
	resp, err := http.Get(targetUrl)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	c.Data(200, "text/plain", body)
}
