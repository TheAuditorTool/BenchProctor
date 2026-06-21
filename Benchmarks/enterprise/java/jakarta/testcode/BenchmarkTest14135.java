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
public class BenchmarkTest14135 {

    @GET
    @Path("/BenchmarkTest14135")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest14135(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        Files.delete(Paths.get("/var/app/data/" + forwardedIp));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
