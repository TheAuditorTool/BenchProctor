// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest21124 {

    private static String trimEnds(String v) { return v.trim(); }

    @GET
    @Path("/BenchmarkTest21124")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21124(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = trimEnds(userId);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
