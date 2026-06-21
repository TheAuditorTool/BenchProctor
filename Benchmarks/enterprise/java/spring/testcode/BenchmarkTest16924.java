// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16924 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest16924/{pathId}")
    public void BenchmarkTest16924(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = trimEnds(pathValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.getWriter().print(processed + ",data\n");
    }
}
