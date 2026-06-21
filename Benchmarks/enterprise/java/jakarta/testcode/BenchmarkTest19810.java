// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest19810 {

    @GET
    @Path("/BenchmarkTest19810")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest19810(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        if (!userId.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        int[] arr = new int[]{10, 20, 30, 40, 50};
        int idx = Integer.parseInt(userId);
        response.setHeader("X-Lookup", String.valueOf(arr[idx]));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
