// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest69751 {

    @PostMapping("/BenchmarkTest69751")
    public void BenchmarkTest69751(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        java.nio.file.Path tmpFile = java.nio.file.Files.createTempFile("app-", ".tmp");
        tmpFile.toFile().deleteOnExit();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
