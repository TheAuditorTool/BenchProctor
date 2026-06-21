// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest62241 {

    @GetMapping("/BenchmarkTest62241")
    public void BenchmarkTest62241(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.function.Function<String, String> preprocessor = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::trim);
        String data = fullPipeline.apply(headerValue);
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) { response.sendError(400); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
