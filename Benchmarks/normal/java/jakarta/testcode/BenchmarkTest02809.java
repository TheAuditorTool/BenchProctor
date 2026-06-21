// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest02809 {

    @POST
    @Path("/BenchmarkTest02809")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02809(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(xmlValue);
        String data = wrapper.toString();
        if (!data.matches("^[\\w\\s<>\\\"'/(){}.*]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        Object evaluated = new jakarta.el.ELProcessor().eval(data);
        return Response.ok("<div>" + evaluated + "</div>", MediaType.TEXT_HTML).build();
    }
}
