// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66118 {

    @GetMapping("/BenchmarkTest66118")
    public void BenchmarkTest66118(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.function.Function<String, String> primary = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> stripChain = primary.andThen(String::strip);
        String data = stripChain.apply(uaValue);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            System.loadLibrary(data);
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
