// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18389 {

    @GetMapping("/BenchmarkTest18389")
    public void BenchmarkTest18389(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        response.setHeader("Access-Control-Allow-Origin", envValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
