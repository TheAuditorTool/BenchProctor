// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest13920 {

    @PostMapping(path="/BenchmarkTest13920", consumes="multipart/form-data")
    public void BenchmarkTest13920(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(uploadName, "http");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        response.sendError(500, data);
    }
}
