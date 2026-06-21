// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18728 {

    @PostMapping(path="/BenchmarkTest18728", consumes="multipart/form-data")
    public void BenchmarkTest18728(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(multipartValue);
        String data = normalizer.apply(multipartValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.sendRedirect(processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
