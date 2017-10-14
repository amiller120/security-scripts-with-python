import time
import sqlite3
import datetime as dt


def output():
    date1 = dt.datetime.now()
    policy = policies()
    source_firewall, source_zone = source_firewalls()
    destination_firewall, destination_zone = destination_firewalls()
    source_address = source_addresses()
    destination_address = destination_addresses()
    port = ports()

    print("\n\nSecurity script 1")
    print("set security policies from-zone {} to-zone {} policy {} "
          "match source-address {} destination-address {} application {}\n"
          "set security policies from-zone {} to-zone {} policy {} "
          "then permit".format(source_zone,
                               "untrust",
                               policy,
                               destination_address,
                               source_address,
                               port,
                               source_zone,
                               "untrust",
                               policy))

    print("\n\nSecurity script 2")
    print("set security policies from-zone {} to-zone {} policy {} match "
          "source-address {} destination-address {} application {}\n"
          "set security policies from-zone {} to-zone {} policy {} "
          "then permit".format("untrust",
                               destination_zone,
                               policy,
                               source_address,
                               destination_address,
                               port,
                               "untrust",
                               destination_zone,
                               policy))

    with sqlite3.connect('security1.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO log (date1, policy, port, source_address, source_zone, "
                  "destination_address, destination_zone) values (?, ?, ?, ?, ?, ?, ?)",
                  (date1, policy, port, source_address, source_zone, destination_address, destination_zone))
        conn.commit()


def policies():
    policy = input("Enter the name of the policy: ")
    return policy


def source_firewalls():
    while True:
        trace_route_question = input("Have you traced the route(s) to the appropriate source firewall(s)? (y/n): ")

        if trace_route_question[0].lower() == 'y':
            firewall_list = ["misc-1", "misc-2", "misc-3", "misc-4", "misc-5"]
            i = 1
            for item in firewall_list:
                print(str(i) + ': ', item)
                i += 1

            loop_on = True
            while loop_on:
                fire_number = (input("Please enter the number associated with the Source firewall in use: "))
                if not fire_number.isdecimal():
                    print("You must enter a valid number.")
                    continue
                fire_number = int(fire_number)
                if 0 < fire_number <= len(firewall_list):
                    firewall = firewall_list[(fire_number - 1)]
                    loop_on = False
                else:
                    print("I\'m sorry that is not a valid option")
                    continue

            # misc-1
            if firewall == 'misc-1':
                misc1_list = ["list", "your", "zones", "here"]
                i = 1
                choice = input("have you traced the zone (y/n)? ")
                if choice.lower() == 'n':
                    print("Please trace the zone and continue.")
                    time.sleep(2)

                for item in misc1_list:
                    print(str(i) + ": ", item)
                    i += 1

                while True:
                    source_number = (input("Please enter the number associated the source zone: "))
                    if not source_number.isdecimal():
                        print("You must enter a valid number.")
                        continue
                    source_number = int(source_number)
                    if 0 < source_number <= len(misc1_list):
                        source_zone = misc1_list[(source_number - 1)]
                        break
                    else:
                        print("I\'m sorry that is not a valid option")
                        continue

            # misc-2
            if firewall == 'misc-2':
                misc2_list = ["list", "your", "zones", "here"]
                i = 1
                choice = input("have you traced the zone (y/n)? ")
                if choice.lower() == 'n':
                    print("Please trace the zone and continue.")
                    time.sleep(2)

                for item in misc2_list:
                    print(str(i) + ": ", item)
                    i += 1

                while True:
                    source_number = (input("Please enter the number associated the source zone: "))
                    if not source_number.isdecimal():
                        print("You must enter a valid number.")
                        continue
                    source_number = int(source_number)
                    if 0 < source_number <= len(misc2_list):
                        source_zone = misc2_list[(source_number - 1)]
                        break
                    else:
                        print("I\'m sorry that is not a valid option")
                        continue

            # misc-3
            if firewall == 'misc-3':
                misc3_list = ["list", "your", "zones", "here"]
                i = 1
                choice = input("have you traced the zone (y/n)? ")
                if choice.lower() == 'n':
                    print("Please trace the zone and continue.")
                    time.sleep(2)

                for item in misc3_list:
                    print(str(i) + ": ", item)
                    i += 1

                while True:
                    source_number = (input("Please enter the number associated the source zone: "))
                    if not source_number.isdecimal():
                        print("You must enter a valid number.")
                        continue
                    source_number = int(source_number)
                    if 0 < source_number <= len(misc3_list):
                        source_zone = misc3_list[(source_number - 1)]
                        break
                    else:
                        print("I\'m sorry that is not a valid option")
                        continue

            # misc-4
            if firewall == 'misc-4':
                misc4_list = ["list", "your", "zones", "here"]
                i = 1
                choice = input("have you traced the zone (y/n)? ")
                if choice.lower() == 'n':
                    print("Please trace the zone and continue.")
                    time.sleep(2)

                for item in misc4_list:
                    print(str(i) + ": ", item)
                    i += 1

                while True:
                    source_number = (input("Please enter the number associated the source zone: "))
                    if not source_number.isdecimal():
                        print("You must enter a valid number.")
                        continue
                    source_number = int(source_number)
                    if 0 < source_number <= len(misc4_list):
                        source_zone = misc4_list[(source_number - 1)]
                        break
                    else:
                        print("I\'m sorry that is not a valid option")
                        continue

            # misc-5
            if firewall == 'misc-5':
                misc5_list = ["list", "your", "zones", "here"]
                i = 1
                choice = input("have you traced the zone (y/n)? ")
                if choice.lower() == 'n':
                    print("Please trace the zone and continue.")
                    time.sleep(2)

                for item in misc5_list:
                    print(str(i) + ": ", item)
                    i += 1

                while True:
                    source_number = (input("Please enter the number associated the source zone: "))
                    if not source_number.isdecimal():
                        print("You must enter a valid number.")
                        continue
                    source_number = int(source_number)
                    if 0 < source_number <= len(misc5_list):
                        source_zone = misc5_list[(source_number - 1)]
                        break
                    else:
                        print("I\'m sorry that is not a valid option")
                        continue

            return firewall, source_zone

        else:
            print("Log into the firewall where the route resides and trace the route.")
            continue


def destination_firewalls():
    while True:
        trace_route_question = input("Have you traced the route(s) to the appropriate destination firewall(s)? (y/n): ")

        if trace_route_question[0].lower() == 'y':
            firewall_list = ["misc-1", "misc-2", "misc-3", "misc-4", "misc-5"]
            i = 1
            for item in firewall_list:
                print(str(i) + ': ', item)
                i += 1

            loop_on = True
            while loop_on:
                fire_number = (input("Please enter the number associated with the Destination firewall in use: "))
                if not fire_number.isdecimal():
                    print("You must enter a valid number.")
                    continue
                fire_number = int(fire_number)
                if 0 < fire_number <= len(firewall_list):
                    firewall = firewall_list[(fire_number - 1)]
                    loop_on = False
                else:
                    print("I\'m sorry that is not a valid option")

            # misc-1
            if firewall == 'misc-1':
                choice = input("have you traced the zone (y/n)? ")
                if choice.lower() == 'n':
                    print("Please trace the zone and continue.")
                    time.sleep(2)

                misc1_list = ["list", "your", "zones", "here"]
                i = 1
                for item in misc1_list:
                    print(str(i) + ": ", item)
                    i += 1

                while True:
                    destination_number = (input("Please enter the number associated the destination zone: "))
                    if not destination_number.isdecimal():
                        print("You must enter a valid number.")
                        continue
                    destination_number = int(destination_number)
                    if 0 < destination_number <= len(misc1_list):
                        destination_zone = misc1_list[(destination_number - 1)]
                        break
                    else:
                        print("I'm sorry that is not a valid option")
                        continue

            # misc-2
            if firewall == 'misc-2':
                choice = input("have you traced the zone (y/n)? ")
                if choice.lower() == 'n':
                    print("Please trace the zone and continue.")
                    time.sleep(2)

                misc2_list = ["list", "your", "zones", "here"]
                i = 1
                for item in misc2_list:
                    print(str(i) + ": ", item)
                    i += 1

                while True:
                    destination_number = (input("Please enter the number associated the destination zone: "))
                    if not destination_number.isdecimal():
                        print("You must enter a valid number.")
                        continue
                    destination_number = int(destination_number)
                    if 0 < destination_number <= len(misc2_list):
                        destination_zone = misc2_list[(destination_number - 1)]
                        break
                    else:
                        print("I'm sorry that is not a valid option")
                        continue

            # misc-3
            if firewall == 'misc-3':
                choice = input("have you traced the zone (y/n)? ")
                if choice.lower() == 'n':
                    print("Please trace the zone and continue.")
                    time.sleep(2)

                misc3_list = ["list", "your", "zones", "here"]
                i = 1
                for item in misc3_list:
                    print(str(i) + ": ", item)
                    i += 1

                while True:
                    destination_number = (input("Please enter the number associated the destination zone: "))
                    if not destination_number.isdecimal():
                        print("You must enter a valid number.")
                        continue
                    destination_number = int(destination_number)
                    if 0 < destination_number <= len(misc3_list):
                        destination_zone = misc3_list[(destination_number - 1)]
                        break
                    else:
                        print("I'm sorry that is not a valid option")
                        continue

            # misc-4
            if firewall == 'misc-4':
                choice = input("have you traced the zone (y/n)? ")
                if choice.lower() == 'n':
                    print("Please trace the zone and continue.")
                    time.sleep(2)

                misc4_list = ["list", "your", "zones", "here"]
                i = 1
                for item in misc4_list:
                    print(str(i) + ": ", item)
                    i += 1

                while True:
                    destination_number = (input("Please enter the number associated the destination zone: "))
                    if not destination_number.isdecimal():
                        print("You must enter a valid number.")
                        continue
                    destination_number = int(destination_number)
                    if 0 < destination_number <= len(misc4_list):
                        destination_zone = misc4_list[(destination_number - 1)]
                        break
                    else:
                        print("I'm sorry that is not a valid option")
                        continue

            # misc-5
            if firewall == 'misc-5':
                choice = input("have you traced the zone (y/n)? ")
                if choice.lower() == 'n':
                    print("Please trace the zone and continue.")
                    time.sleep(2)

                misc5_list = ["list", "your", "zones", "here"]
                i = 1
                for item in misc5_list:
                    print(str(i) + ": ", item)
                    i += 1

                while True:
                    destination_number = (input("Please enter the number associated the destination zone: "))
                    if not destination_number.isdecimal():
                        print("You must enter a valid number.")
                        continue
                    destination_number = int(destination_number)
                    if 0 < destination_number <= len(misc5_list):
                        destination_zone = misc5_list[(destination_number - 1)]
                        break
                    else:
                        print("I'm sorry that is not a valid option")
                        continue

            return firewall, destination_zone

        else:
            print("Please trace the appropriate routes and restart program.")
            continue


def source_addresses():
    while True:
        source = input("Do you know the source address? (y/n): ").strip()
        if source[0].lower() == 'y':
            source_address = input("Enter the first source address with the appropriate mask if needed: ")
            break

        else:
            print("Please get the source address.")
            continue

    return source_address


def destination_addresses():
    while True:
        destination = input("Do you know the destination address? (y/n): ").strip()
        if destination[0].lower() == 'y':
            destination_address = input("Enter the first destination address with the appropriate mask if needed: ")
            break

        else:
            print("Please get the destination address.")
            continue

    return destination_address


def ports():
    port = input("What is the port?: ")
    return port


output()
