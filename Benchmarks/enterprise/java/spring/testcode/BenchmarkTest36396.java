// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36396 {

    @GetMapping("/BenchmarkTest36396")
    public void BenchmarkTest36396(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String argValue = java.util.Optional.ofNullable(System.getProperty("argv.value", "")).orElse("");
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(argValue, "header");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        new ProcessBuilder("echo", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
