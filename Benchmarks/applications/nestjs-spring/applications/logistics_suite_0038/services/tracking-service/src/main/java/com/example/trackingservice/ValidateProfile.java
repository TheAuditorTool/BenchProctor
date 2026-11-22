// SPDX-License-Identifier: Apache-2.0
package com.example.trackingservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ValidateProfile {


    @GetMapping("/ValidateProfile")
    public void validateProfile(@javax.validation.constraints.Size(max = 4096) @RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = xCustomHeader != null ? xCustomHeader : "";
        String consignment;
        if (wording.length() > 256) { consignment = wording.substring(0, 256); }
        else { consignment = wording; }
        response.getWriter().print("<div>" + consignment + "</div>");
    }
}
