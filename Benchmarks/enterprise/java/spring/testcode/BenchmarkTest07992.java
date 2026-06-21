// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest07992 {

    @GetMapping("/BenchmarkTest07992")
    public void BenchmarkTest07992(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.function.Function<String, String> firstStage = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(headerValue);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            response.getWriter().print("<div>" + data + "</div>");
        }
    }
}
