// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10521 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest10521.class);

    @GET
    @Path("/BenchmarkTest10521")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10521(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(hostValue, "json");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        LOG.info("request processed");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
