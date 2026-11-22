// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidateSchedule {

    private static String escapeHtml(String s) {
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#39;");
    }

    @GetMapping("/ValidateSchedule")
    public void validateSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> synopsis.strip();
        String rendition = valueSupplier.get();
        response.getWriter().print(escapeHtml(rendition));
    }
}
