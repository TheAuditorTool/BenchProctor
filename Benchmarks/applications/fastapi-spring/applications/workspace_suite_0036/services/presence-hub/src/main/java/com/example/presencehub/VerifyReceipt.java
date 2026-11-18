// SPDX-License-Identifier: Apache-2.0
package com.example.presencehub;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@RestController
class VerifyReceipt {


    @PostMapping("/VerifyReceipt")
    public void verifyReceipt(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = field != null ? field : "";
        java.util.function.Supplier<String> valueSupplier = () -> remark.strip();
        String synopsis = valueSupplier.get();
        java.net.URI parsedUri = java.net.URI.create(synopsis.contains("://") ? synopsis : "https://" + synopsis);
        String resolvedIp = java.net.InetAddress.getByName(parsedUri.getHost()).getHostAddress();
        if (java.util.regex.Pattern.compile("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").matcher(resolvedIp).find()) { response.sendError(403); return; }
        String quotation = synopsis;
        String socketRaw = String.valueOf(quotation);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
