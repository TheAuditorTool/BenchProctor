// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest01113 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest01113.class);

    @GET
    @Path("/BenchmarkTest01113")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest01113(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = forwardedIp.isEmpty() ? "default" : forwardedIp;
        LOG.info("request processed");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
