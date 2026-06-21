// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest34057 {

    @GetMapping("/BenchmarkTest34057")
    public void BenchmarkTest34057(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = "" + originValue;
        new java.io.File("/tmp/" + data).createNewFile();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
