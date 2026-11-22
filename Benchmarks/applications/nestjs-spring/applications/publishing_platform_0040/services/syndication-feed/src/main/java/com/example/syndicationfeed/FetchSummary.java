// SPDX-License-Identifier: Apache-2.0
package com.example.syndicationfeed;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class FetchSummary {

    private static String escapeHtml(String s) {
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#39;");
    }

    @GetMapping("/FetchSummary")
    public void fetchSummary(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> transcript.strip();
        String addendum = valueSupplier.get();
        response.getWriter().print(escapeHtml(addendum));
    }
}
