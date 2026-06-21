// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52813 {

    @GetMapping("/BenchmarkTest52813")
    public void BenchmarkTest52813(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String prefix = uaValue.length() > 0 ? uaValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = uaValue.toLowerCase(); break;
            case "f": data = uaValue.toUpperCase(); break;
            default: data = uaValue.strip(); break;
        }
        new ProcessBuilder("python3", "-c", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
