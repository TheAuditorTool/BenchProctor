// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64689 {

    @GetMapping("/BenchmarkTest64689")
    public void BenchmarkTest64689(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        response.setHeader("Access-Control-Allow-Origin", uaValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
