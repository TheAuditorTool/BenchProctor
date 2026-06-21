// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22547 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest22547")
    public void BenchmarkTest22547(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        holder.set(refererValue);
        String data = holder.get();
        if (!data.matches("^[\\w\\s<>\\\"'/().;=]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        response.getWriter().print("<div>" + data + "</div>");
    }
}
