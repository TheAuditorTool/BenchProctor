// SPDX-License-Identifier: Apache-2.0
package com.example.partnerregistry;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class EnrichConfig {


    @GetMapping("/EnrichConfig")
    public void enrichConfig(@javax.validation.constraints.Size(max = 4096) @RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = xCustomHeader != null ? xCustomHeader : "";
        String handshake;
        if (citation.length() > 256) { handshake = citation.substring(0, 256); }
        else { handshake = citation; }
        response.getWriter().print("<div>" + handshake + "</div>");
    }
}
