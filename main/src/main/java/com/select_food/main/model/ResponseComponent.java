package com.select_food.main.model;

import java.util.List;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ResponseComponent {
    public String MenuId;
    public String MenuName;
    public String RestaurantName;
    public String Img;
    public String Carbo;
    public String Protain;
    public String Lipid;
    public List<Integer> TagId;
}
