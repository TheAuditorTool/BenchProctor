// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01260 {

    private static final java.util.concurrent.atomic.AtomicReference<String> ref = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest01260")
    public void BenchmarkTest01260(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        ref.set(authHeader);
        String data = ref.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        byte[] buf = new byte[Integer.parseInt(processed)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
