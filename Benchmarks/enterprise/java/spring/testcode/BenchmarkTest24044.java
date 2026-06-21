// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest24044 {

    @GetMapping("/BenchmarkTest24044")
    public void BenchmarkTest24044(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        java.nio.file.Path tmpFile = java.nio.file.Files.createTempFile("app-", ".tmp");
        tmpFile.toFile().deleteOnExit();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
