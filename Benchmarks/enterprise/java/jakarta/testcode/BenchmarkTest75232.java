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
public class BenchmarkTest75232 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest75232")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest75232(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String stdinValue = java.util.Optional.ofNullable(new java.util.Scanner(System.in).nextLine()).orElse("");
        String data = normalize(stdinValue);
        Files.delete(Paths.get("/var/app/data/" + data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
