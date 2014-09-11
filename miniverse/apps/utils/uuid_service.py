from datetime import datetime
import uuid

def generate_storage_identifier():
    """
    Make a UUID based on the host ID and current time

    e.g. 'f7e666ee-395a-11e4-b09d-3c15c2b7e55c'

    """
    return str(uuid.uuid1())

"""
/*
    e.g. 147d9f71e1c-ce103e2365f6
*/
public String generateStorageIdentifier() {
        String storageIdentifier = null;

        UUID uid = UUID.randomUUID();

        logger.info("UUID value: "+uid.toString());

        // last 6 bytes, of the random UUID, in hex:

        String hexRandom = uid.toString().substring(24);

        logger.info("UUID (last 6 bytes, 12 hex digits): "+hexRandom);

        String hexTimestamp = Long.toHexString(new Date().getTime());

        logger.info("(not UUID) timestamp in hex: "+hexTimestamp);

        storageIdentifier = hexTimestamp + "-" + hexRandom;

        logger.info("timestamp/UUID hybrid: "+storageIdentifier);
        return storageIdentifier;
    }
"""