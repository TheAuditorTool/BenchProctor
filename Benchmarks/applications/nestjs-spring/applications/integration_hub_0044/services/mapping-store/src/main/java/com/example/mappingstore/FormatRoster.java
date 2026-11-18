// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatRoster {


    @GetMapping("/FormatRoster/{pathId}")
    public void formatRoster(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String blurb = pathId;
        String handshake = java.net.URLDecoder.decode(blurb, java.nio.charset.StandardCharsets.UTF_8);
        String citation = handshake.matches("^(plain|markdown|html|text)$") ? handshake : "plain";
        response.getWriter().print("<div>" + citation + "</div>");
    }
}
