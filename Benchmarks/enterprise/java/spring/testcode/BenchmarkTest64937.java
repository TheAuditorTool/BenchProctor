// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64937 {

    @GetMapping("/BenchmarkTest64937")
    public void BenchmarkTest64937(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.function.Function<String, String> firstStage = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::trim);
        String data = composed.apply(uaValue);
        String normalizedPath = java.nio.file.Paths.get(data).normalize().toString();
        new java.io.File("/tmp/" + normalizedPath).createNewFile();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
