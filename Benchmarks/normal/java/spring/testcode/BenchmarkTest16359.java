// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest16359 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @PostMapping(path="/BenchmarkTest16359", consumes="multipart/form-data")
    public void BenchmarkTest16359(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data = collapseWhitespace(uploadName);
        response.setHeader("Access-Control-Allow-Origin", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
