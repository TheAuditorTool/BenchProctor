// SPDX-License-Identifier: Apache-2.0
package com.example.fxservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactReceipt {


    @GetMapping("/CompactReceipt")
    public void compactReceipt(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = id != null ? id : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(headline, "body");
        String disbursement = entry.getKey();
        response.getWriter().print("<div>" + disbursement + "</div>");
    }
}
