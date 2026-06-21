// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest20839 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest20839.class);

    @GET
    @Path("/BenchmarkTest20839")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest20839(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String prefix = originValue.length() > 0 ? originValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = originValue.toLowerCase(); break;
            case "f": data = originValue.toUpperCase(); break;
            default: data = originValue.strip(); break;
        }
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
