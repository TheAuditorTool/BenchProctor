// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63995 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest63995")
    public void BenchmarkTest63995(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        holder.set(userId);
        String data = holder.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setHeader("Refresh", "0; url=" + processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
