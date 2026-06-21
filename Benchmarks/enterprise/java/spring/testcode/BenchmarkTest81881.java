// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81881 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest81881")
    public void BenchmarkTest81881(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        holder.set(uaValue);
        String data = holder.get();
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException nfe) {
            response.sendError(400, "invalid number"); return;
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
