// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportDigest {


    @GetMapping("/ExportDigest")
    public void exportDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(citation, "http");
        String backorder = tuple.getKey();
        if (!backorder.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + backorder + "</div>");
    }
}
