package com.select_food.main.model;

//import java.util.List;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;

@Getter
@Entity
@Table(name = "menu") public class Menu {
    
    @Id
    @Column(name = "id")
    private String menuId;

    @Column(name = "menu")
    private String menuName;
    
}
