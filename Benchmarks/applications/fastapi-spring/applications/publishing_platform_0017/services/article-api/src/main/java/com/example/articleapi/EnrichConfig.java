// SPDX-License-Identifier: Apache-2.0
package com.example.articleapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@RestController
class EnrichConfig {


    @PostMapping("/EnrichConfig")
    public void enrichConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = field != null ? field : "";
        java.util.function.Supplier<String> valueSupplier = () -> summary.strip();
        String addendum = valueSupplier.get();
        java.net.URI parsedUri = java.net.URI.create(addendum.contains("://") ? addendum : "https://" + addendum);
        String resolvedIp = java.net.InetAddress.getByName(parsedUri.getHost()).getHostAddress();
        if (java.util.regex.Pattern.compile("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").matcher(resolvedIp).find()) { response.sendError(403); return; }
        String byline = addendum;
        String socketRaw = String.valueOf(byline);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
