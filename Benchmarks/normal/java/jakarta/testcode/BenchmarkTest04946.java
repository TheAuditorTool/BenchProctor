// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04946 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest04946.class);

    @GET
    @Path("/BenchmarkTest04946")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04946(@QueryParam("items") java.util.List<String> items, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String queryArray = items.get(0) != null ? items.get(0) : "";
        String prefix = queryArray.length() > 0 ? queryArray.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = queryArray.toLowerCase(); break;
            case "f": data = queryArray.toUpperCase(); break;
            default: data = queryArray.strip(); break;
        }
        String processed = data.replace("\r", "").replace("\n", "").replaceAll("[A-Za-z0-9]{4,}", "****");
        LOG.info("Action: {}", processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
