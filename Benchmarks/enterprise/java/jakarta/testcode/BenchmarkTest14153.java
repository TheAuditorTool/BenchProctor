// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest14153 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest14153.class);

    @GET
    @Path("/BenchmarkTest14153")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest14153(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String prefix = headerValue.length() > 0 ? headerValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = headerValue.toLowerCase(); break;
            case "f": data = headerValue.toUpperCase(); break;
            default: data = headerValue.strip(); break;
        }
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
