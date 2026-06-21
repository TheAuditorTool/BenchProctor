// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest30536 {

    @GET
    @Path("/BenchmarkTest30536")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest30536(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        new java.io.File(forwardedIp).delete();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
