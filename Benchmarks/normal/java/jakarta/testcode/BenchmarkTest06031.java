// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest06031 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest06031.class);

    @GET
    @Path("/BenchmarkTest06031")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest06031(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String prefix = cookieValue.length() > 0 ? cookieValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = cookieValue.toLowerCase(); break;
            case "f": data = cookieValue.toUpperCase(); break;
            default: data = cookieValue.strip(); break;
        }
        LOG.info("request processed");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
