// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50070 {

    @PostMapping(path="/BenchmarkTest50070", consumes="application/xml")
    public void BenchmarkTest50070(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.function.Function<String, String> tabNormalizer = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::strip);
        String data = decorated.apply(xmlValue);
        response.sendError(500, data);
    }
}
