// SPDX-License-Identifier: Apache-2.0
package com.example.customsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@RestController
class EnrichBundle {


    @PostMapping("/EnrichBundle")
    public void enrichBundle(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = field != null ? field : "";
        java.util.function.Supplier<String> valueSupplier = () -> phrase.strip();
        String parcel = valueSupplier.get();
        java.net.URI parsedUri = java.net.URI.create(parcel.contains("://") ? parcel : "https://" + parcel);
        String resolvedIp = java.net.InetAddress.getByName(parsedUri.getHost()).getHostAddress();
        if (java.util.regex.Pattern.compile("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").matcher(resolvedIp).find()) { response.sendError(403); return; }
        String consignment = parcel;
        String socketRaw = String.valueOf(consignment);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
