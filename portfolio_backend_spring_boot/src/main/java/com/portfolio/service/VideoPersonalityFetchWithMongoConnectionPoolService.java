package com.portfolio.service;

import com.mongodb.client.MongoCollection;
import com.portfolio.converter.VideoPersonalityConverter;
import com.portfolio.util.MessagePrettifier;
import org.bson.Document;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.Map;

import static com.mongodb.client.model.Filters.eq;



@Service
public class VideoPersonalityFetchWithMongoConnectionPoolService {
    private static final Logger MYAPP_LOGGER = LoggerFactory.getLogger("myapp");

    private final MongoCollection<Document> characterAPersonalityCollection;
    private final VideoPersonalityConverter videoPersonalityConverter;
    private final MessagePrettifier messagePrettifier;

    public VideoPersonalityFetchWithMongoConnectionPoolService(
            MongoCollection<Document> characterAPersonalityCollection,
            VideoPersonalityConverter videoPersonalityConverter
    ) {
        this.characterAPersonalityCollection = characterAPersonalityCollection;
        this.videoPersonalityConverter = videoPersonalityConverter;
        this.messagePrettifier = new MessagePrettifier("printingToLog");
    }

    public Map<String, Object> fetchVideoPersonality(String videoPersonalityDocId) {
        Document videoPersonalityDoc = characterAPersonalityCollection.find(eq("_id", videoPersonalityDocId)).first();

        if (videoPersonalityDoc == null) {
            MYAPP_LOGGER.info("videoPersonalityDocId: {}, fetched from mongodb:\n{}", videoPersonalityDocId, messagePrettifier.prettifyJson(videoPersonalityDoc));
            return null;
        }

        MYAPP_LOGGER.info("videoPersonalityDocId: {}, fetched from mongodb:\n{}", videoPersonalityDocId, messagePrettifier.prettifyJson(videoPersonalityDoc));
        return videoPersonalityConverter.convertDocumentToResponseMap(videoPersonalityDoc);
    }
}
