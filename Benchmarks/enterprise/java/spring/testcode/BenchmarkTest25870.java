// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest25870 {

    @PostMapping(path="/BenchmarkTest25870", consumes="multipart/form-data")
    public void BenchmarkTest25870(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> uploadName)
            .thenApply(v -> v.length() > 256 ? v.substring(0, 256).strip() : v.strip())
            .join();
        response.setHeader("Refresh", "0; url=" + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
