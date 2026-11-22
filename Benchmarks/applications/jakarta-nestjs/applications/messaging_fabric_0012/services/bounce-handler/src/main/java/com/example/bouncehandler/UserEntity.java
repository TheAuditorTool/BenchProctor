package com.example.bouncehandler;

@jakarta.persistence.Entity(name = "User")
@jakarta.persistence.Table(name = "users")
public class UserEntity {

    @jakarta.persistence.Id
    private Integer id;

    private String name;

    private String role;

    private String bio;

    private String email;

    public Integer getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getRole() {
        return role;
    }

    public String getBio() {
        return bio;
    }

    public String getEmail() {
        return email;
    }
}
