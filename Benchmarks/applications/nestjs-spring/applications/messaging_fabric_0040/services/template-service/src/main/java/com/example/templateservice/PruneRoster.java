// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PruneRoster {


    @GetMapping("/PruneRoster/{pathId}")
    public void pruneRoster(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = pathId;
        String bulletin = java.net.URLDecoder.decode(preface, java.nio.charset.StandardCharsets.UTF_8);
        String notice = bulletin.matches("^(plain|markdown|html|text)$") ? bulletin : "plain";
        response.getWriter().print("<div>" + notice + "</div>");
    }
}
