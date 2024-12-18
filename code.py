from time import sleep

from thumb import can, lights

led = lights.get_led()
can_bus = can.get_can_bus()
while True:
    with can_bus.listen(timeout=0.5) as listener:
        message_count = listener.in_waiting()
        print(message_count, "messages available")
        if message_count == 0:
            lights.flash(led)
            continue
        for _i in range(message_count):
            msg = listener.receive()
            if msg.id == can.MESSAGE_ADDRESS:
                cruise_state = can.extract_cruise_state(msg.data)
                if cruise_state in (can.CruiseState.OFF,):
                    led.value = True
                else:
                    led.value = False
    sleep(0.5)
