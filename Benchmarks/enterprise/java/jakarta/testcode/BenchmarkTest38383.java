// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest38383 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest38383")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest38383(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = stripWhitespace(forwardedIp);
        return Response.status(500).entity(data).build();
    }
}
