package com.select_food.main.model;

import lombok.Getter;

@Getter
public class RequestComponent {
    public static class userLocation {
        public Double latitude;
        public Double longitude;
    }
    private Double latitude;
    private Double longitude;
    private int userDisease;
    private int userAllergy;
    private int userReligion;
    private Boolean userVegan;
}
