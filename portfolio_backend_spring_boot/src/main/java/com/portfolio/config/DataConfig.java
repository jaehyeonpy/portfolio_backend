package com.portfolio.config;

import com.mongodb.MongoClientSettings;
import com.mongodb.ServerAddress;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.List;



@Configuration
public class DataConfig {
    @Value("${app.data.mongodb.host}")
    private String mongoHost;

    @Value("${app.data.mongodb.port}")
    private int mongoPort;

    @Value("${app.data.mongodb.max-pool-size}")
    private int mongoMaxPoolSize;

    @Value("${app.data.mongodb.database}")
    private String mongoDatabaseName;

    @Value("${app.data.mongodb.collection}")
    private String mongoCollectionName;

    @Bean
    public MongoClient mongoClient() {
        MongoClientSettings settings = MongoClientSettings.builder()
                .applyToClusterSettings(builder -> builder.hosts(List.of(new ServerAddress(mongoHost, mongoPort))))
                .applyToConnectionPoolSettings(builder -> builder.maxSize(mongoMaxPoolSize))
                .build();

        return MongoClients.create(settings);
    }

    @Bean
    public MongoDatabase personalityDatabase(MongoClient mongoClient) {
        return mongoClient.getDatabase(mongoDatabaseName);
    }

    @Bean
    public MongoCollection<Document> characterAPersonalityCollection(MongoDatabase personalityDatabase) {
        return personalityDatabase.getCollection(mongoCollectionName);
    }
}
