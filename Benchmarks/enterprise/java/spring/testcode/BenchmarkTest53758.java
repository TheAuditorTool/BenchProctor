// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest53758 {

    @GetMapping("/BenchmarkTest53758")
    public void BenchmarkTest53758(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String prefix = refererValue.length() > 0 ? refererValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = refererValue.toLowerCase(); break;
            case "f": data = refererValue.toUpperCase(); break;
            default: data = refererValue.strip(); break;
        }
        response.setHeader("Refresh", "0; url=" + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
