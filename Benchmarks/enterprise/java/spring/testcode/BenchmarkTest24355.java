// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest24355 {

    @GetMapping("/BenchmarkTest24355")
    public void BenchmarkTest24355(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.function.Function<String, String> tabNormalizer = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::strip);
        String data = decorated.apply(cookieValue);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            response.getWriter().print("<div>" + data + "</div>");
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
    }
}
