// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest44349 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest44349/{pathId}")
    public void BenchmarkTest44349(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        response.getWriter().print(data + ",data\n");
    }
}
