// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66018 {

    @GetMapping("/BenchmarkTest66018")
    public void BenchmarkTest66018(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(hostValue);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
