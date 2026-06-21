// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60234 {

    @GetMapping("/BenchmarkTest60234")
    public void BenchmarkTest60234(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        if ("https://app.acmecdn.net".equals(uaValue)) response.setHeader("Access-Control-Allow-Origin", uaValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
