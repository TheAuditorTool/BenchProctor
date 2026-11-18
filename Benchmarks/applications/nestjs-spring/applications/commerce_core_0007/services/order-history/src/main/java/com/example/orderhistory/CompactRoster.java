// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class CompactRoster {


    @GetMapping("/CompactRoster")
    public void compactRoster(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = java.util.Optional.ofNullable(System.getenv("ORDERS_INPUT_0007")).orElse("");
        String prefix = heading.length() > 0 ? heading.substring(0, 1).toLowerCase() : "";
        String voucher;
        switch (prefix) {
            case "h": voucher = heading.toLowerCase(); break;
            case "f": voucher = heading.toUpperCase(); break;
            default: voucher = heading.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(voucher);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
