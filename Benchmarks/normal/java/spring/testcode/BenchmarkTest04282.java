// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04282 {

    @PostMapping(path="/BenchmarkTest04282", consumes="multipart/form-data")
    public void BenchmarkTest04282(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.function.Function<String, String> firstStage = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(multipartValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(processed).find()) {
            response.setHeader("X-Validated-Input", processed);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
