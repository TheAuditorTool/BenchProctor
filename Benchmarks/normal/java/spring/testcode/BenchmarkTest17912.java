// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17912 {

    @GetMapping("/BenchmarkTest17912")
    public void BenchmarkTest17912(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String configValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.json")))).orElse("");
        String prefix = configValue.length() > 0 ? configValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = configValue.toLowerCase(); break;
            case "f": data = configValue.toUpperCase(); break;
            default: data = configValue.strip(); break;
        }
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(data);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
