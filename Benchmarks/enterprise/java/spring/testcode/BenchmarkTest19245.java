// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest19245 {

    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping("/BenchmarkTest19245")
    public void BenchmarkTest19245(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        sharedRef.set(fieldValue);
        String data = sharedRef.get();
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException nfe) {
            response.sendError(400, "invalid number"); return;
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
