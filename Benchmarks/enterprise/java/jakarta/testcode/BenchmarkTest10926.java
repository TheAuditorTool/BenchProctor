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
public class BenchmarkTest10926 {

    @GET
    @Path("/BenchmarkTest10926")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10926(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        System.loadLibrary(forwardedIp);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
