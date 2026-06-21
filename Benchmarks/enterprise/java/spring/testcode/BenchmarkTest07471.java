// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest07471 {

    @PostMapping(path="/BenchmarkTest07471", consumes="application/xml")
    public void BenchmarkTest07471(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.function.Function<String, String> preprocessor = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::strip);
        String data = fullPipeline.apply(xmlValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setHeader("Access-Control-Allow-Origin", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
