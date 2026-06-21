// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest07861 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest07861")
    public void BenchmarkTest07861(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        valueRef.set(authHeader);
        String data = valueRef.get();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + data});
            pb.redirectErrorStream(true);
            pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
