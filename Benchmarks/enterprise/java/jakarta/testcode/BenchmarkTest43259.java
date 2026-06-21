// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest43259 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest43259.class);

    @GET
    @Path("/BenchmarkTest43259")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest43259(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        LOG.info("Action: {}", userId);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
