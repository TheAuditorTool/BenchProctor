// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest43962 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest43962.class);

    @GET
    @Path("/BenchmarkTest43962")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest43962(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = String.join(" ", headerValue.split("\\s+"));
        LOG.info("request processed");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
