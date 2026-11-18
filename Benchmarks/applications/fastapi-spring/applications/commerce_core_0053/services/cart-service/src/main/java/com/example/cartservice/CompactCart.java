// SPDX-License-Identifier: Apache-2.0
package com.example.cartservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactCart {


    @GetMapping("/CompactCart")
    public void compactCart(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(memo, "cookie");
        String voucher = kv.getKey();
        if (!voucher.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + voucher + "</div>");
    }
}
