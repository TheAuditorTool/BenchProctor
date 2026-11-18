// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FetchLedger {


    @GetMapping("/FetchLedger")
    public void fetchLedger(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = id != null ? id : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(passage, "body");
        String montage = tuple.getKey();
        response.getWriter().print("<div>" + montage + "</div>");
    }
}
