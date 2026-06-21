// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16488 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GetMapping("/BenchmarkTest16488")
    public void BenchmarkTest16488(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = toLowerCase(uaValue);
        new java.io.File("/tmp/" + data).createNewFile();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
