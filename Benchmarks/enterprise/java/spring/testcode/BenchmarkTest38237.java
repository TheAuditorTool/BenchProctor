// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38237 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest38237")
    public void BenchmarkTest38237(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String stdinValue = java.util.Optional.ofNullable(new java.util.Scanner(System.in).nextLine()).orElse("");
        holder.set(stdinValue);
        String data = holder.get();
        if (System.currentTimeMillis() > 1000000000000L) {
            ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + data});
            pb.redirectErrorStream(true);
            pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
