from nordvpn_switcher_plus import initialize_VPN, rotate_VPN, terminate_VPN
from dotenv import load_dotenv
import os

load_dotenv()

class NordVPN:
    settings = None

    def connect(self):
        self.settings = initialize_VPN(save=1, area_input=[
                                       "complete rotation"], skip_settings=1, login=os.environ['LOGIN'], password=os.environ['PASSWORD'])
        self.rotate()

    def rotate(self):
        rotate_VPN(instructions=self.settings)

    def disconnect(self):
        terminate_VPN(instructions=self.settings)
