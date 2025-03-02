import logging
import time

from actions.base import ActionConfig, ActionConnector
from actions.move.interface import MoveInput


class MoveRos2Connector(ActionConnector[MoveInput]):

    def __init__(self, config: ActionConfig):
        super().__init__(config)

    async def connect(self, output_interface: MoveInput) -> None:

        new_msg = {"move": ""}

        # stub to show how to do this
        if output_interface.action == "move forward":
            new_msg["move"] = "move forward"
        elif output_interface.action == "turn":
            new_msg["move"] = "turn"
        else:
            logging.info(f"Other move type: {output_interface.action}")
            # raise ValueError(f"Unknown move type: {output_interface.action}")

        logging.info(f"SendThisToROS2: {new_msg}")

    def tick(self) -> None:
        time.sleep(0.1)
        # logging.info("MoveRos2Connector Tick")