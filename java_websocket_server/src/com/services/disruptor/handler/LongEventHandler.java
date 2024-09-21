package com.services.disruptor.handler;

import com.lmax.disruptor.EventHandler;
import com.services.disruptor.event.LongEvent;

public class LongEventHandler implements EventHandler<LongEvent> {
    @Override
    public void onEvent(LongEvent event, long sequence, boolean endOfBatch) throws Exception {
        System.out.println("Event: " + event);
    }
}
