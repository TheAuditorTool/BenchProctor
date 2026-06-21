// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest53532 {

    @PostMapping(path="/BenchmarkTest53532", consumes="text/plain")
    public void BenchmarkTest53532(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = "" + rawData;
        new java.io.File("/tmp/" + data).createNewFile();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
