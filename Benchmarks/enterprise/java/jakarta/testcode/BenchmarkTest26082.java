// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest26082 {

    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @GET
    @Path("/BenchmarkTest26082")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest26082(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String prefix = cookieValue.length() > 0 ? cookieValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = cookieValue.toLowerCase(); break;
            case "f": data = cookieValue.toUpperCase(); break;
            default: data = cookieValue.strip(); break;
        }
        sharedLastValue = data;
        int seen = sharedWriteCount;
        sharedWriteCount = seen + 1;
        return Response.ok().build();
    }
}
