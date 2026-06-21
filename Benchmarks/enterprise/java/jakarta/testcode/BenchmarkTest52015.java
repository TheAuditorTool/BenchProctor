// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest52015 {

    @GET
    @Path("/BenchmarkTest52015")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest52015(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(forwardedIp, "request");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        request.setAttribute("hidden_form_field", data);
        request.getRequestDispatcher("/dashboard").forward(request, response);
        return Response.noContent().build();
    }
}
