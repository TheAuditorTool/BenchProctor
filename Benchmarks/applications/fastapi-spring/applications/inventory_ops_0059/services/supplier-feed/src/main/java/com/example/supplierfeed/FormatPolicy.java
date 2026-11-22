// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatPolicy {


    @PostMapping(path="/FormatPolicy", consumes="text/plain")
    public void formatPolicy(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = rawBody != null ? rawBody : "";
        byte[] raw = memo.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String backorder = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        String restock = backorder.matches("^(plain|markdown|html|text)$") ? backorder : "plain";
        response.getWriter().print("<div>" + restock + "</div>");
    }
}
