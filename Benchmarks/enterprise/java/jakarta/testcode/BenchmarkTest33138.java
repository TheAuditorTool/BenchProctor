// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest33138 {

    @GET
    @Path("/BenchmarkTest33138")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest33138(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String apiBody = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(new java.net.URL("https://api.svc.local/data").openStream())).readLine()).orElse("");
        String prefix = apiBody.length() > 0 ? apiBody.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = apiBody.toLowerCase(); break;
            case "f": data = apiBody.toUpperCase(); break;
            default: data = apiBody.strip(); break;
        }
        Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
