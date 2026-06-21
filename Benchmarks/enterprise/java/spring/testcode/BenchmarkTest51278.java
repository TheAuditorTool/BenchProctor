// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51278 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest51278")
    public void BenchmarkTest51278(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        stateBox.set(uaValue);
        String data = stateBox.get();
        if (System.currentTimeMillis() > 1000000000000L) {
            Files.delete(Paths.get("/var/app/data/" + data));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
