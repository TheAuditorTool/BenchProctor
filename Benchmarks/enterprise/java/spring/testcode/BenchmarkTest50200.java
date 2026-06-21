// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50200 {

    @PostMapping("/BenchmarkTest50200")
    public void BenchmarkTest50200(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        StringBuilder carrier = new StringBuilder();
        carrier.append(commentValue);
        String data = carrier.toString();
        if (System.currentTimeMillis() > 1000000000000L) {
            new ProcessBuilder("python3", "-c", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
