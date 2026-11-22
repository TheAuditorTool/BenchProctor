// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00078 {

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

    private static String normalize(String v) { return v.strip(); }

    @POST
    @Path("/BenchmarkTest00078/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00078(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = normalize(commentValue);
        javax.xml.stream.XMLInputFactory staxFactory = javax.xml.stream.XMLInputFactory.newInstance();
        javax.xml.stream.XMLStreamReader staxReader = staxFactory.createXMLStreamReader(new java.io.StringReader(data));
        StringBuilder xmlText = new StringBuilder();
        while (staxReader.hasNext()) { if (staxReader.next() == javax.xml.stream.XMLStreamConstants.CHARACTERS) { xmlText.append(staxReader.getText()); } }
        response.setHeader("X-Xml-Text-Length", String.valueOf(xmlText.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
