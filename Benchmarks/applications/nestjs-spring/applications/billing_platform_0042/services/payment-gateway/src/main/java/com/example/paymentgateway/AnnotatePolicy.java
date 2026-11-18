// SPDX-License-Identifier: Apache-2.0
package com.example.paymentgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AnnotatePolicy {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/AnnotatePolicy", consumes="text/plain")
    public void annotatePolicy(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = rawBody != null ? rawBody : "";
        String remittance = normalize(remark);
        if (!remittance.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + remittance + "</div>");
    }
}
