// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CollectSchedule {


    @GetMapping("/CollectSchedule")
    public void collectSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = authorization != null ? authorization : "";
        String backorder;
        try { backorder = new String(java.util.Base64.getDecoder().decode(citation), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { backorder = citation; }
        response.getWriter().print("<div>" + backorder + "</div>");
    }
}
