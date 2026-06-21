// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest80090 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest80090.class);

    @GET
    @Path("/BenchmarkTest80090")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest80090(@QueryParam("items") java.util.List<String> items, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String queryArray = items.get(0) != null ? items.get(0) : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + queryArray;
        String data = valueSupplier.get();
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
