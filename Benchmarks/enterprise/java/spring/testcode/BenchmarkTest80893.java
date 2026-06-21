// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80893 {

    @GetMapping("/BenchmarkTest80893/{pathId}")
    public void BenchmarkTest80893(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        response.getWriter().print(pathValue + ",data\n");
    }
}
