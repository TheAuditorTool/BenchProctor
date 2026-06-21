// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50484 {

    @GetMapping("/BenchmarkTest50484")
    public void BenchmarkTest50484(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        if ("admin".equals(uaValue)) {
            response.getWriter().print("{\"role\":\"admin\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
