// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class PruneManifest {

    private static String escapeHtml(String s) {
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#39;");
    }

    @GetMapping("/PruneManifest")
    public void pruneManifest(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> transcript.strip();
        String consignment = valueSupplier.get();
        response.getWriter().print(escapeHtml(consignment));
    }
}
