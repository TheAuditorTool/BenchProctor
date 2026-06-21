// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest20543 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest20543.class);

    @GET
    @Path("/BenchmarkTest20543")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest20543(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        String data = propValue.isEmpty() ? "default" : propValue;
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
