// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"net/url"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00125(c *gin.Context) {
	pathValue := c.Param("id")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(pathValue)
	parsedURL, parseErr := url.Parse(data)
	if parseErr != nil || (parsedURL.Scheme != "http" && parsedURL.Scheme != "https") || parsedURL.User != nil || strings.ContainsAny(data, "\\ \t\r\n") || !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	upstreamReq, err := http.NewRequest(http.MethodGet, targetUrl, nil)
	if err != nil {
		c.String(http.StatusBadRequest, err.Error())
		return
	}
	upstreamReq.Header.Set("Accept", "application/json")
	resp, err := http.DefaultClient.Do(upstreamReq)
	if err != nil {
		c.String(http.StatusBadGateway, err.Error())
		return
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	c.Data(200, "text/plain", body)
}
