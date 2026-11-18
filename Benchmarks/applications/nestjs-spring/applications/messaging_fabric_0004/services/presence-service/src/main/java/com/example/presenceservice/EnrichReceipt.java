// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EnrichReceipt {


    @GetMapping("/EnrichReceipt/{pathId}")
    public void enrichReceipt(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = pathId;
        String bulletin = java.net.URLDecoder.decode(paragraph, java.nio.charset.StandardCharsets.UTF_8);
        String synopsis = bulletin.matches("^(plain|markdown|html|text)$") ? bulletin : "plain";
        response.getWriter().print("<div>" + synopsis + "</div>");
    }
}
