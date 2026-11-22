// SPDX-License-Identifier: Apache-2.0
package com.example.carriergateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuditShipment {


    @GetMapping("/AuditShipment")
    public void auditShipment(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String quotation = xCustomHeader != null ? xCustomHeader : "";
        String parcel;
        if (quotation.length() > 256) { parcel = quotation.substring(0, 256); }
        else { parcel = quotation; }
        response.getWriter().print("<div>" + parcel + "</div>");
    }
}
