// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00063(c *gin.Context) {
	_apiResp, _apiErr := http.Get("https://api.svc.cluster/data")
	if _apiErr != nil {
		return
	}
	defer _apiResp.Body.Close()
	_apiBytes, _ := io.ReadAll(_apiResp.Body)
	apiValue := string(_apiBytes)
	data := fmt.Sprintf("%s", apiValue)
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	c.Redirect(http.StatusFound, targetUrl)
}
