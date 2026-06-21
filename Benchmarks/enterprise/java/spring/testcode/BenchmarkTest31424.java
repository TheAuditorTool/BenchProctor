// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest31424 {

    @PostMapping(path="/BenchmarkTest31424", consumes="text/plain")
    public void BenchmarkTest31424(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.function.Function<String, String> initialFn = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::strip);
        String data = transformed.apply(rawData);
        if (!data.matches("^[\\w\\s./\\\\:_?&=\\-@]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        response.sendRedirect(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
