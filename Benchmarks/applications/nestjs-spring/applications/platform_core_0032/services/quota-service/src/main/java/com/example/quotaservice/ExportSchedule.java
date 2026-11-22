// SPDX-License-Identifier: Apache-2.0
package com.example.quotaservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportSchedule {

    private static String escapeHtml(String s) {
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#39;");
    }

    @GetMapping("/ExportSchedule")
    public void exportSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> remark.strip();
        String persona = valueSupplier.get();
        response.getWriter().print(escapeHtml(persona));
    }
}
