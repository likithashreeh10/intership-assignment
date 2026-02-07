class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"

    def set_password(self, new_password):
        self.__password = new_password
        print("Password updated successfully!")


account = InstagramAccount("naina_insta", "1234")

account.add_private_reel("Beach Reel")
account.add_private_reel("Food Reel")

account.add_archived_reel("Old Travel Reel")
account.add_archived_reel("College Memories Reel")

account.display_private_reels(True)
account.display_private_reels(False)

account.display_archived_reels("1234")
account.display_archived_reels("0000")

account.set_password("5678")

account.display_archived_reels("5678")
