// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51785 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @PostMapping("/BenchmarkTest51785")
    public void BenchmarkTest51785(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        try { AllowedValue.valueOf(commentValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { commentValue = AllowedValue.values()[0].name().toLowerCase(); }
        new ProcessBuilder("python3", "-c", commentValue).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
