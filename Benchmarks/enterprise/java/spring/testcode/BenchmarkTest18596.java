// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest18596 {

    @PostMapping(path="/BenchmarkTest18596", consumes="multipart/form-data")
    public void BenchmarkTest18596(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        StringBuilder payload = new StringBuilder();
        payload.append(uploadName);
        String data = payload.toString();
        response.sendError(500, data);
    }
}
