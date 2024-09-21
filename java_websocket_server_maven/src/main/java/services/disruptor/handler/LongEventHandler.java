package services.disruptor.handler;

import com.lmax.disruptor.EventHandler;
import services.disruptor.event.LongEvent;

public class LongEventHandler implements EventHandler<LongEvent> {
    @Override
    public void onEvent(LongEvent event, long sequence, boolean endOfBatch) {
        System.out.println("Event: " + event);
    }
}

