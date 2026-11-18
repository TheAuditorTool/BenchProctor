// SPDX-License-Identifier: Apache-2.0
package com.example.retryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class LoadBundle {


    @GetMapping("/LoadBundle/{pathId}")
    public void loadBundle(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = pathId;
        String handshake = java.net.URLDecoder.decode(synopsis, java.nio.charset.StandardCharsets.UTF_8);
        String memo = handshake.matches("^(plain|markdown|html|text)$") ? handshake : "plain";
        response.getWriter().print("<div>" + memo + "</div>");
    }
}
