// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75758 {

    @GetMapping("/BenchmarkTest75758")
    public void BenchmarkTest75758(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        java.nio.file.Path tmpFile = java.nio.file.Files.createTempFile("app-", ".tmp");
        tmpFile.toFile().deleteOnExit();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
