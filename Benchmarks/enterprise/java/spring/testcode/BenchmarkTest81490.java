// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest81490 {

    @PostMapping(path="/BenchmarkTest81490", consumes="multipart/form-data")
    public void BenchmarkTest81490(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(uploadName);
        String data = normalizer.apply(uploadName);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            response.getWriter().print("<div>" + data + "</div>");
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
    }
}
