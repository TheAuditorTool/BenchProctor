// SPDX-License-Identifier: Apache-2.0
package com.example.anomalyscorer;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@RestController
class RotateDigest {


    @PostMapping("/RotateDigest")
    public void rotateDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = field != null ? field : "";
        java.util.function.Supplier<String> valueSupplier = () -> caption.strip();
        String cohort = valueSupplier.get();
        java.net.URI parsedUri = java.net.URI.create(cohort.contains("://") ? cohort : "https://" + cohort);
        String resolvedIp = java.net.InetAddress.getByName(parsedUri.getHost()).getHostAddress();
        if (java.util.regex.Pattern.compile("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").matcher(resolvedIp).find()) { response.sendError(403); return; }
        String gauge = cohort;
        String socketRaw = String.valueOf(gauge);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
