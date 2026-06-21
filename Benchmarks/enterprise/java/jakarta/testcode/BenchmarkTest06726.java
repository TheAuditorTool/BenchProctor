// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest06726 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest06726.class);

    @GET
    @Path("/BenchmarkTest06726")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest06726(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        LOG.info("Action: {}", forwardedIp);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
