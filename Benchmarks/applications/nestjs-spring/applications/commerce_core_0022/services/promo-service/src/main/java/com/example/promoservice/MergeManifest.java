// SPDX-License-Identifier: Apache-2.0
package com.example.promoservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@RestController
class MergeManifest {


    @GetMapping("/MergeManifest")
    public void mergeManifest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = origin != null ? origin : "";
        java.util.function.Supplier<String> valueSupplier = () -> subject.strip();
        String voucher = valueSupplier.get();
        String socketRaw = String.valueOf(voucher);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
