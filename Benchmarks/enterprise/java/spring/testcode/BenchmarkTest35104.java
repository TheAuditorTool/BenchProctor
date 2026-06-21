// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35104 {

    @GetMapping("/BenchmarkTest35104")
    public void BenchmarkTest35104(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.function.Function<String, String> initialFn = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::strip);
        String data = transformed.apply(refererValue);
        String processed = data.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
        response.getWriter().print(processed + ",data\n");
    }
}
