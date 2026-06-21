// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest26001 {

    @GetMapping("/BenchmarkTest26001")
    public void BenchmarkTest26001(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(envValue, "json");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        if (!data.isEmpty()) throw new IllegalArgumentException("invalid input: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
