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
public class BenchmarkTest00011 {

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
    @Path("/BenchmarkTest00011")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00011(@jakarta.validation.constraints.Size(max = 4096) String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = xmlValue.replace("\u0000", "");
        StringBuilder xmlText = new StringBuilder();
        javax.xml.parsers.SAXParser saxParser = javax.xml.parsers.SAXParserFactory.newInstance().newSAXParser();
        saxParser.parse(new org.xml.sax.InputSource(new java.io.StringReader(data)), new org.xml.sax.helpers.DefaultHandler() { @Override public void characters(char[] ch, int start, int length) { xmlText.append(ch, start, length); } });
        response.setHeader("X-Xml-Text-Length", String.valueOf(xmlText.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
