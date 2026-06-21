// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18331 {

    @GET
    @Path("/BenchmarkTest18331/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18331(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String prefix = pathValue.length() > 0 ? pathValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = pathValue.toLowerCase(); break;
            case "f": data = pathValue.toUpperCase(); break;
            default: data = pathValue.strip(); break;
        }
        int[] arr = new int[]{10, 20, 30, 40, 50};
        int idx = Integer.parseInt(data);
        response.setHeader("X-Lookup", String.valueOf(arr[idx]));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
