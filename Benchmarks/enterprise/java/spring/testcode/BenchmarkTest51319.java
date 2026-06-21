// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51319 {

    @PostMapping("/BenchmarkTest51319")
    public void BenchmarkTest51319(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(commentValue);
        String data = normalizer.apply(commentValue);
        int boundedVal;
        try { boundedVal = Integer.parseInt(data); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        if (boundedVal < 0 || boundedVal > 1048576) { response.sendError(400); return; }
        long requested = boundedVal;
        long allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
