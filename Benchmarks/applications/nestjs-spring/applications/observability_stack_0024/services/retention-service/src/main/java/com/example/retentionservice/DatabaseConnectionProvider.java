package com.example.retentionservice;

public class DatabaseConnectionProvider implements org.hibernate.engine.jdbc.connections.spi.ConnectionProvider, org.hibernate.service.spi.Configurable {

    private String databaseUrlVariable;

    private String fallbackUrl;

    private String fallbackUser;

    private String fallbackPassword;

    @Override
    public void configure(java.util.Map<String, Object> settings) {
        databaseUrlVariable = (String) settings.get("app.datasource.url_env");
        fallbackUrl = (String) settings.get("jakarta.persistence.jdbc.url");
        fallbackUser = (String) settings.get("jakarta.persistence.jdbc.user");
        fallbackPassword = (String) settings.get("jakarta.persistence.jdbc.password");
    }

    @Override
    public java.sql.Connection getConnection() throws java.sql.SQLException {
        String dbUrl = System.getenv(databaseUrlVariable);
        if (dbUrl != null && dbUrl.startsWith("postgres")) {
            java.net.URI dbUri = java.net.URI.create(dbUrl);
            String dbUserInfo = dbUri.getUserInfo() != null ? dbUri.getUserInfo() : "app:app";
            int dbSep = dbUserInfo.indexOf(':');
            int dbPort = dbUri.getPort() == -1 ? 5432 : dbUri.getPort();
            return java.sql.DriverManager.getConnection(
                "jdbc:postgresql://" + dbUri.getHost() + ":" + dbPort + dbUri.getPath() + "?" + (dbUri.getRawQuery() == null ? "" : dbUri.getRawQuery() + "&") + "stringtype=unspecified",
                dbSep < 0 ? dbUserInfo : dbUserInfo.substring(0, dbSep),
                dbSep < 0 ? "" : dbUserInfo.substring(dbSep + 1));
        }
        return java.sql.DriverManager.getConnection(fallbackUrl, fallbackUser, fallbackPassword);
    }

    @Override
    public void closeConnection(java.sql.Connection connection) throws java.sql.SQLException {
        connection.close();
    }

    @Override
    public boolean supportsAggressiveRelease() {
        return false;
    }

    @Override
    public boolean isUnwrappableAs(Class<?> unwrapType) {
        return false;
    }

    @Override
    public <T> T unwrap(Class<T> unwrapType) {
        throw new org.hibernate.service.UnknownUnwrapTypeException(unwrapType);
    }
}
