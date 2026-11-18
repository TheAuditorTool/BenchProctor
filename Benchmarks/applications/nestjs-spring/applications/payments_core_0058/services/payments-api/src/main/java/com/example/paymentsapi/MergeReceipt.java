// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class MergeReceipt {


    @GetMapping("/MergeReceipt")
    public void mergeReceipt(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = java.util.Optional.ofNullable(System.getenv("PAYMENTS_INPUT_0058")).orElse("");
        String prefix = caption.length() > 0 ? caption.substring(0, 1).toLowerCase() : "";
        String ledger;
        switch (prefix) {
            case "h": ledger = caption.toLowerCase(); break;
            case "f": ledger = caption.toUpperCase(); break;
            default: ledger = caption.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(ledger);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
