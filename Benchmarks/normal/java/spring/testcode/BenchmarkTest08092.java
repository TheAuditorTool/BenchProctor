// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest08092 {

    @PostMapping(path="/BenchmarkTest08092", consumes="multipart/form-data")
    public void BenchmarkTest08092(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(uploadName);
        String data = bundle.toString();
        response.sendError(500, data);
    }
}
