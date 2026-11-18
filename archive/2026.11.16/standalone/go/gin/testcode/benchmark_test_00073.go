// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net"
	"net/http"
	"net/url"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00073(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", authHeader)
	data := relayBuilder.String()
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
	conn, err := net.Dial("tcp", targetUrl)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
