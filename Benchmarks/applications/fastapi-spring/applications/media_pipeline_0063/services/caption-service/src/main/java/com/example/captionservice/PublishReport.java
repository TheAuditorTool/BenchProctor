// SPDX-License-Identifier: Apache-2.0
package com.example.captionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PublishReport {


    @GetMapping("/PublishReport")
    public void publishReport(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = id != null ? id : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : snippet.split(",")) { tokens.add(token.trim()); }
        String montage = String.join(",", tokens);
        response.getWriter().print("<div>" + montage + "</div>");
    }
}
