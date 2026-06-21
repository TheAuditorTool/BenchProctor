// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12473 {

    @GetMapping("/BenchmarkTest12473")
    public void BenchmarkTest12473(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        response.setHeader("Access-Control-Allow-Origin", uaValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
