package com.select_food.main.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
@Entity
@Getter
@Table(name = "sample_tag_info")
public class taginfo {
    @Id
    @Column(name = "menuid")
    public String MenuId;
    @Column(name = "tagid")
    public Integer TagId;
}
