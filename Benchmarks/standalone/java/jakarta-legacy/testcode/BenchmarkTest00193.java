// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.container.ContainerRequestContext;
import javax.ws.rs.container.ContainerRequestFilter;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00193 {

    @Provider
    public static class BindingRestrictionFilter implements ContainerRequestFilter {
        @Override
        public void filter(ContainerRequestContext requestContext) {
            requestContext.getHeaders().remove("X-Internal-Bind");
        }
    }

    @Provider
    public static class FailureMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception ex) {
            return Response.status(500).entity("request failed").build();
        }
    }

    @POST
    @Path("/BenchmarkTest00193/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00193(@javax.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(commentValue, "json");
        String data = kv.getKey();
        if (!("true".equals(data) || "false".equals(data))) { return Response.status(400).build(); }
        String displayName = data.matches("[A-Za-z][A-Za-z .'-]{0,63}") ? data.strip() : "guest";
        request.getSession().setAttribute("displayName", displayName);
        String greetingName = String.valueOf(request.getSession().getAttribute("displayName"));
        return Response.ok("{\"greetingLength\":" + greetingName.length() + "}", MediaType.APPLICATION_JSON).build();
    }
}
