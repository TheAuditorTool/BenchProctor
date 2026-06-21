// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60886 {

    @GetMapping("/BenchmarkTest60886")
    public void BenchmarkTest60886(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String apiBody = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(new java.net.URL("https://api.svc.local/data").openStream())).readLine()).orElse("");
        String prefix = apiBody.length() > 0 ? apiBody.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = apiBody.toLowerCase(); break;
            case "f": data = apiBody.toUpperCase(); break;
            default: data = apiBody.strip(); break;
        }
        Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
