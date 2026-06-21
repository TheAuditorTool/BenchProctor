// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09225 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest09225.class);

    @GET
    @Path("/BenchmarkTest09225")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09225(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String prefix = forwardedIp.length() > 0 ? forwardedIp.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = forwardedIp.toLowerCase(); break;
            case "f": data = forwardedIp.toUpperCase(); break;
            default: data = forwardedIp.strip(); break;
        }
        String processed = data.replace("\r", "").replace("\n", "").replaceAll("[A-Za-z0-9]{4,}", "****");
        LOG.info("Action: {}", processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
