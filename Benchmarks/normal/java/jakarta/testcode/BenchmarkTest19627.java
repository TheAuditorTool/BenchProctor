// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest19627 {

    @GET
    @Path("/BenchmarkTest19627")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest19627(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String prefix = originValue.length() > 0 ? originValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = originValue.toLowerCase(); break;
            case "f": data = originValue.toUpperCase(); break;
            default: data = originValue.strip(); break;
        }
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        request.setAttribute("hidden_form_field", data);
        request.getRequestDispatcher("/dashboard").forward(request, response);
        return Response.noContent().build();
    }
}
