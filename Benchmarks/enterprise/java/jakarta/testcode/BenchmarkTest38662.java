// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest38662 {

    @GET
    @Path("/BenchmarkTest38662")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest38662(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        if (!refererValue.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        int[] arr = new int[]{10, 20, 30, 40, 50};
        int idx = Integer.parseInt(refererValue);
        response.setHeader("X-Lookup", String.valueOf(arr[idx]));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
