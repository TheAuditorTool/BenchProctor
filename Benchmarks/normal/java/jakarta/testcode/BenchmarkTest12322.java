// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest12322 {

    @GET
    @Path("/BenchmarkTest12322")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12322(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = String.join(" ", userId.split("\\s+"));
        java.util.HashMap<String,Object> entity = new java.util.HashMap<>();
        String[] kv = data.split("=", 2);
        if (kv.length == 2) {
            entity.put(kv[0], kv[1]);
            response.setHeader("X-Field-Set", kv[0]);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
