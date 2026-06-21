// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51515 {

    @GetMapping("/BenchmarkTest51515")
    public void BenchmarkTest51515(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Function<String, String> tabNormalizer = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::strip);
        String data = decorated.apply(userId);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setHeader("X-Forwarded-For", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
