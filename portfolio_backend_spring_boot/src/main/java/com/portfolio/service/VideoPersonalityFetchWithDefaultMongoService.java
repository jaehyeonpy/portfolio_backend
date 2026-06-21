package com.portfolio.service;

import com.mongodb.MongoClientSettings;
import com.mongodb.ServerAddress;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.portfolio.converter.VideoPersonalityConverter;
import com.portfolio.util.MessagePrettifier;
import org.bson.Document;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import static com.mongodb.client.model.Filters.eq;



@Service
public class VideoPersonalityFetchWithDefaultMongoService {
    private static final Logger MYAPP_LOGGER = LoggerFactory.getLogger("myapp");

    private final VideoPersonalityConverter videoPersonalityConverter;
    private final MessagePrettifier messagePrettifier;

    @Value("${app.data.mongodb.host}")
    private String mongoHost;

    @Value("${app.data.mongodb.port}")
    private int mongoPort;

    @Value("${app.data.mongodb.database}")
    private String mongoDatabaseName;

    @Value("${app.data.mongodb.collection}")
    private String mongoCollectionName;

    public VideoPersonalityFetchWithDefaultMongoService(VideoPersonalityConverter videoPersonalityConverter) {
        this.videoPersonalityConverter = videoPersonalityConverter;
        this.messagePrettifier = new MessagePrettifier("printingToLog");
    }

    public Map<String, Object> fetchVideoPersonality(String videoPersonalityDocId) {
        MongoClientSettings settings =
                MongoClientSettings.builder()
                        .applyToClusterSettings(builder ->
                                builder.hosts(List.of(new ServerAddress(mongoHost, mongoPort)))
                                      .serverSelectionTimeout(
                                              Long.MAX_VALUE,
                                              TimeUnit.MILLISECONDS))
                        .applyToSocketSettings(builder ->
                                builder.connectTimeout(0, TimeUnit.MILLISECONDS)
                                       .readTimeout(0, TimeUnit.MILLISECONDS))
                        .build();

        try (MongoClient mongoClient = MongoClients.create(settings)) {
            Document videoPersonalityDoc = mongoClient
                    .getDatabase(mongoDatabaseName)
                    .getCollection(mongoCollectionName)
                    .find(eq("_id", videoPersonalityDocId))
                    .first();

            
            if (videoPersonalityDoc == null) {
                MYAPP_LOGGER.info("videoPersonalityDocId: {}, fetched from mongodb:\n{}", videoPersonalityDocId, messagePrettifier.prettifyJson(videoPersonalityDoc));
                return null;
            }

            MYAPP_LOGGER.info("videoPersonalityDocId: {}, fetched from mongodb:\n{}", videoPersonalityDocId, messagePrettifier.prettifyJson(videoPersonalityDoc));
            return videoPersonalityConverter.convertDocumentToResponseMap(videoPersonalityDoc);
        }
    }
}
