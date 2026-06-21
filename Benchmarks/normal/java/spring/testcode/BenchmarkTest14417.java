// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14417 {

    @GetMapping("/BenchmarkTest14417")
    public void BenchmarkTest14417(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(refererValue);
        String data = normalizer.apply(refererValue);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            new Socket(data, 80).close();
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
