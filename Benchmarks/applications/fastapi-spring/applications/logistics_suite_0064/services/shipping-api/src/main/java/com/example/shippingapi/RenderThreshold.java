// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderThreshold {


    @GetMapping("/RenderThreshold")
    public void renderThreshold(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = userAgent != null ? userAgent : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", transcript);
        String parcel = sw.toString();
        response.getWriter().print("<div>" + parcel + "</div>");
    }
}
