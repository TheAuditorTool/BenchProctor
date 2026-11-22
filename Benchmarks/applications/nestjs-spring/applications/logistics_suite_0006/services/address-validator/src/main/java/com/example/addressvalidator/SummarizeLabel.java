// SPDX-License-Identifier: Apache-2.0
package com.example.addressvalidator;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class SummarizeLabel {


    @GetMapping("/SummarizeLabel")
    public void summarizeLabel(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = xCustomHeader != null ? xCustomHeader : "";
        String consignment;
        if (summary.length() > 256) { consignment = summary.substring(0, 256); }
        else { consignment = summary; }
        response.getWriter().print("<div>" + consignment + "</div>");
    }
}
