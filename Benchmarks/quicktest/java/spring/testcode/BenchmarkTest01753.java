// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01753 {

    @GetMapping("/BenchmarkTest01753")
    public void BenchmarkTest01753(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String stdinValue = java.util.Optional.ofNullable(new java.util.Scanner(System.in).nextLine()).orElse("");
        java.util.Properties box = new java.util.Properties();
        box.load(new java.io.StringReader("rawValue=" + stdinValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", box.getProperty("format", "plain"));
        String data = box.getProperty("rawValue", "");
        Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
