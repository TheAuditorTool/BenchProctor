// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest76816 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest76816.class);

    @GET
    @Path("/BenchmarkTest76816")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest76816(@QueryParam("items") java.util.List<String> items, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String queryArray = items.get(0) != null ? items.get(0) : "";
        StringBuilder payload = new StringBuilder();
        payload.append(queryArray);
        String data = payload.toString();
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
