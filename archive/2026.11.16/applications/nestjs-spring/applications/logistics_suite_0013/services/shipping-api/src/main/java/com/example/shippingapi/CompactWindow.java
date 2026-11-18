// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactWindow {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/CompactWindow")
    public void compactWindow(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = userAgent != null ? userAgent : "";
        String parcel = normalize(footnote);
        response.getWriter().print("<div>" + parcel + "</div>");
    }
}
