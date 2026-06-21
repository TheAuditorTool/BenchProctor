// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest45180 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest45180.class);

    @GET
    @Path("/BenchmarkTest45180")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest45180(@QueryParam("items") java.util.List<String> items, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String queryArray = items.get(0) != null ? items.get(0) : "";
        String data = "[%s]".formatted(queryArray);
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
