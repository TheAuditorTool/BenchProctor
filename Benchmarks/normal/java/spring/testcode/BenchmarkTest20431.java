// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20431 {

    @GetMapping("/BenchmarkTest20431/{pathId}")
    public void BenchmarkTest20431(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Function<String, String> preprocessor = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::strip);
        String data = fullPipeline.apply(pathValue);
        response.sendError(500, data);
    }
}
