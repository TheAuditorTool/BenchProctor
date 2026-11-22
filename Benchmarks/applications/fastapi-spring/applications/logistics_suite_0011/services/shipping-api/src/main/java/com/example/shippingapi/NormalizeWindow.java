// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class NormalizeWindow {


    @PostMapping(path="/NormalizeWindow", consumes="text/plain")
    public void normalizeWindow(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = rawBody != null ? rawBody : "";
        byte[] raw = citation.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String consignment = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        String parcel = consignment.matches("^(plain|markdown|html|text)$") ? consignment : "plain";
        response.getWriter().print("<div>" + parcel + "</div>");
    }
}
