// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.net.*;

@RestController
class AuditRoster {


    @GetMapping("/AuditRoster")
    public void auditRoster(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = origin != null ? origin : "";
        java.util.function.Supplier<String> valueSupplier = () -> citation.strip();
        String consignment = valueSupplier.get();
        String socketRaw = String.valueOf(consignment);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
