// SPDX-License-Identifier: Apache-2.0
package com.example.customsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EnrichRoster {


    @GetMapping("/EnrichRoster/{pathId}")
    public void enrichRoster(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = pathId;
        String parcel = java.net.URLDecoder.decode(phrase, java.nio.charset.StandardCharsets.UTF_8);
        String consignment = parcel.matches("^(plain|markdown|html|text)$") ? parcel : "plain";
        response.getWriter().print("<div>" + consignment + "</div>");
    }
}
