package com.select_food.main.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.select_food.main.model.Menu;


@Repository
public interface MenuRepo extends JpaRepository<Menu,String>{
    @Query("SELECT r.menuName FROM Menu r WHERE r.menuId = :id")
    List<String> findNamesByMenuId(@Param("id") String id);
}
