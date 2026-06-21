// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04681 {

    @GetMapping("/BenchmarkTest04681")
    public void BenchmarkTest04681(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        StringBuilder payload = new StringBuilder();
        payload.append(authHeader);
        String data = payload.toString();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            String content = Files.readString(Paths.get("/var/app/data/" + data), java.nio.charset.StandardCharsets.UTF_8);
            response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
