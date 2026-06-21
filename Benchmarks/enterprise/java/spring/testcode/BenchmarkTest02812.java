// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02812 {

    @GetMapping("/BenchmarkTest02812")
    public void BenchmarkTest02812(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(userId);
        String data = normalizer.apply(userId);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        request.getSession().setAttribute("data", String.valueOf(processed));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
