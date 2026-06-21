// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest03156 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest03156.class);

    @GET
    @Path("/BenchmarkTest03156")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03156(@QueryParam("items") java.util.List<String> items, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String queryArray = items.get(0) != null ? items.get(0) : "";
        LOG.info("Action: {}", queryArray);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
