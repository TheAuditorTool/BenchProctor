// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36901 {

    @GetMapping("/BenchmarkTest36901/{pathId}")
    public void BenchmarkTest36901(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Function<String, String> preprocessor = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::trim);
        String data = fullPipeline.apply(pathValue);
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + data}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
