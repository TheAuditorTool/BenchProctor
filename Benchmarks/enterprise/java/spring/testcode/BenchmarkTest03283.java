// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03283 {

    @GetMapping("/BenchmarkTest03283/{pathId}")
    public void BenchmarkTest03283(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        StringBuilder envelope = new StringBuilder();
        envelope.append(pathValue);
        String data = envelope.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        new java.io.File("/tmp/" + processed).createNewFile();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
