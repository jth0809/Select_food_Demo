package com.select_food.main.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.select_food.main.model.taginfo;

@Repository
public interface TagRepo extends JpaRepository<taginfo,Integer> {
    @Query("SELECT DISTINCT r.MenuId FROM taginfo r WHERE r.TagId = :id")
    List<Integer> findid(@Param("id") int id);
    @Query("SELECT r.TagId FROM taginfo r WHERE r.MenuId = :id")
    List<Integer> findtagid(@Param("id") String id);
    @Query("SELECT DISTINCT r.MenuId FROM taginfo r")
    List<Integer> findallid();
}
