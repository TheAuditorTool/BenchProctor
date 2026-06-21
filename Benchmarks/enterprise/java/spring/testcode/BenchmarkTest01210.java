// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest01210 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest01210.class);

    @PostMapping(path="/BenchmarkTest01210", consumes="multipart/form-data")
    public void BenchmarkTest01210(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String prefix = uploadName.length() > 0 ? uploadName.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = uploadName.toLowerCase(); break;
            case "f": data = uploadName.toUpperCase(); break;
            default: data = uploadName.strip(); break;
        }
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
