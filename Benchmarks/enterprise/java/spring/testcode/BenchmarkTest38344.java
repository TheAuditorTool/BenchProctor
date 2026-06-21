// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38344 {

    private static String trimEnds(String v) { return v.trim(); }

    @PostMapping("/BenchmarkTest38344")
    public void BenchmarkTest38344(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = trimEnds(commentValue);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            System.loadLibrary(data);
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
