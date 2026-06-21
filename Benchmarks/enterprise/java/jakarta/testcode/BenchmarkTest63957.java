// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest63957 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest63957.class);

    @GET
    @Path("/BenchmarkTest63957")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest63957(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data;
        if (forwardedIp.length() > 256) { data = forwardedIp.substring(0, 256); }
        else { data = forwardedIp; }
        LOG.info("request processed");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
