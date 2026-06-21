// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12961 {

    @GetMapping("/BenchmarkTest12961")
    public void BenchmarkTest12961(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String prefix = refererValue.length() > 0 ? refererValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = refererValue.toLowerCase(); break;
            case "f": data = refererValue.toUpperCase(); break;
            default: data = refererValue.strip(); break;
        }
        System.setProperty("app.user.preference", data);
        response.setHeader("X-Config-Set", "app.user.preference");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
