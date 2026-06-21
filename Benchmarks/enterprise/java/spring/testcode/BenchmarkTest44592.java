// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest44592 {

    @GetMapping("/BenchmarkTest44592")
    public void BenchmarkTest44592(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String prefix = hostValue.length() > 0 ? hostValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = hostValue.toLowerCase(); break;
            case "f": data = hostValue.toUpperCase(); break;
            default: data = hostValue.strip(); break;
        }
        System.setProperty("app.user.preference", data);
        response.setHeader("X-Config-Set", "app.user.preference");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
