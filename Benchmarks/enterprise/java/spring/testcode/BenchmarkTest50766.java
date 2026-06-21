// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50766 {

    @GetMapping("/BenchmarkTest50766")
    public void BenchmarkTest50766(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + uaValue + "\"}");
    }
}
