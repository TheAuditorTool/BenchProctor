// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04181 {

    @GetMapping("/BenchmarkTest04181")
    public void BenchmarkTest04181(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String apiBody = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(new java.net.URL("https://api.svc.local/data").openStream())).readLine()).orElse("");
        java.util.function.Function<String, String> preprocessor = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::trim);
        String data = fullPipeline.apply(apiBody);
        if (System.currentTimeMillis() > 1000000000000L) {
            response.sendRedirect(data);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
