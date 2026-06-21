// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23154 {

    @GetMapping("/BenchmarkTest23154")
    public void BenchmarkTest23154(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : originValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        new ProcessBuilder("echo", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
