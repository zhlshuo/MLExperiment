package org.example;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import com.lmax.disruptor.BlockingWaitStrategy;
import com.lmax.disruptor.EventHandler;
import com.lmax.disruptor.RingBuffer;
import com.lmax.disruptor.dsl.Disruptor;
import com.lmax.disruptor.dsl.ProducerType;
import com.lmax.disruptor.util.DaemonThreadFactory;
import services.disruptor.event.WebSocketEvent;
import services.disruptor.handler.WebSocketEventHandler;
import services.websocket.HelloEndPoint;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws Exception{
        int bufferSize = 1024;

        Disruptor<WebSocketEvent> disruptor = new Disruptor<>(WebSocketEvent::new, bufferSize, DaemonThreadFactory.INSTANCE, ProducerType.SINGLE, new BlockingWaitStrategy());
        WebSocketEventHandler handler = new WebSocketEventHandler();
        disruptor.handleEventsWith(handler);
        disruptor.start();

        RingBuffer<WebSocketEvent> ringBuffer = disruptor.getRingBuffer();

        int port = 5001;
        HelloEndPoint endPoint = new HelloEndPoint(port, ringBuffer);
        endPoint.start();
    }
}