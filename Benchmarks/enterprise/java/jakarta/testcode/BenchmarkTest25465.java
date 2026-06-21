// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest25465 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GET
    @Path("/BenchmarkTest25465")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest25465(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        FormData payload = new FormData(userId);
        String data = payload.payload;
        java.util.Set<String> allowed = java.util.Set.of("name", "email", "bio");
        if (!allowed.contains(data)) { return Response.status(400).build(); }
        java.util.HashMap<String,Object> entity = new java.util.HashMap<>();
        String[] formPair = data.split("=", 2);
        if (formPair.length == 2) {
            entity.put(formPair[0], formPair[1]);
            response.setHeader("X-Field-Set", formPair[0]);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
