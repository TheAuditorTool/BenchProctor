package com.example.releaseapi;

public class JakartaBootstrap {

    @javax.ws.rs.Path("/health")
    public static class HealthResource {
        @javax.ws.rs.GET
        public javax.ws.rs.core.Response health() {
            return javax.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.releaseapi.JakartaBootstrap$HealthResource,com.example.releaseapi.BuildSummary,com.example.releaseapi.CutRelease,com.example.releaseapi.ExportReport,com.example.releaseapi.FormatSummary,com.example.releaseapi.MergeCanary,com.example.releaseapi.MergeWindow,com.example.releaseapi.NormalizeConfig,com.example.releaseapi.PublishSnapshot");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
