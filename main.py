from fingerprint import Scanner
from databaseManager import addNewUser, getUserId

def main():
    # Test enrolment
    scanner = Scanner()
    print("\n\nRegister new user")
    pos = scanner.enrollFingerprint()
    id = input("User id: ")
    addNewUser(pos, id)
    print("\n\nGet user id")
    id = getUserId(scanner.searchFinger())
    print(id)
    print("Id: ", id)


if __name__ == "__main__":
    main()
