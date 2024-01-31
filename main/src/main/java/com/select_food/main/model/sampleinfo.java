package com.select_food.main.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;

@Getter
@Entity
@Table(name = "sample")
public class sampleinfo {
    @Id
    @Column(name = "MENUId")
    public String MenuId;
    @Column(name = "MENUNAME")
    public String MenuName;
    @Column(name = "restaurantname")
    public String RestaurantName;
    @Column(name = "img")
    public String Img;
    @Column(name = "carbo")
    public String Carbo;
    @Column(name = "protain")
    public String Protain;
    @Column(name = "lipid")
    public String Lipid;
}
