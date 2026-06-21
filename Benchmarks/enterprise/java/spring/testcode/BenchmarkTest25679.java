// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest25679 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest25679")
    public void BenchmarkTest25679(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        holder.set(originValue);
        String data = holder.get();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
