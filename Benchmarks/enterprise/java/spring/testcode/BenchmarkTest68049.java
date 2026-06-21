// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest68049 {

    @GetMapping("/BenchmarkTest68049")
    public void BenchmarkTest68049(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.function.Function<String, String> initialFn = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::trim);
        String data = transformed.apply(uaValue);
        if (System.currentTimeMillis() > 1000000000000L) {
            response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
        }
    }
}
