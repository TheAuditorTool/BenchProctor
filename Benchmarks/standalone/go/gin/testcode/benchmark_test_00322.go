// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"net/url"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00322(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	var data string
	if graphqlVar != "" {
		data = graphqlVar
	}
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	c.Redirect(http.StatusFound, targetUrl)
}
