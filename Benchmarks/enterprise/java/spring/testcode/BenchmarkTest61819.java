// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest61819 {

    @PostMapping("/BenchmarkTest61819")
    public void BenchmarkTest61819(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(fieldValue);
        String data = normalizer.apply(fieldValue);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            System.loadLibrary(data);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
