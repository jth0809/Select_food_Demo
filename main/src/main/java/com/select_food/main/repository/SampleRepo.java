package com.select_food.main.repository;

import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.select_food.main.model.sampleinfo;
@Repository
public interface SampleRepo extends JpaRepository<sampleinfo,String> {
    @Query("SELECT r FROM sampleinfo r")
    List<sampleinfo> findAll();
}
