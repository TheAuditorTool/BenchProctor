// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01098 {

    @GetMapping("/BenchmarkTest01098")
    public void BenchmarkTest01098(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String apiBody = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(new java.net.URL("https://api.svc.local/data").openStream())).readLine()).orElse("");
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{apiBody});
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        data = safeMapper.readValue(data.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(data);
    }
}
