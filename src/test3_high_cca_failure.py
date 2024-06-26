from calculations import calculate_transmission_time

CCA = 150                         # ms
CCA_PROBABILITY_FAILURE = 0.8

PACKET_RECEIVED_PROBABILITY=0
RECEIVER_NOT_IN_CHANNEL=0

GUARD_TIME = 3                    # ms
PACKET_SIZE = 1280 * 8            # convert bytes to bits

if __name__ == "__main__":
    # Nodes in the network
    nodes = list(range(1, 27))   # 1 to 26

    # Possible routes from 17 to 21
    route1 = [17, 13, 14, 15, 21]
    route2 = [17, 18, 19, 20, 21]
    route3 = [17, 12, 7, 2, 1, 6, 11, 16, 21]

    # Calculate transmission times for each route
    # Print the results
    time_route1, _ = calculate_transmission_time(24, CCA, CCA_PROBABILITY_FAILURE, PACKET_SIZE, GUARD_TIME, PACKET_RECEIVED_PROBABILITY, RECEIVER_NOT_IN_CHANNEL)
    print(f"Transmission time for RPL Operation: {time_route1:.2f} ms")

    time_route2, _ = calculate_transmission_time(10, CCA, CCA_PROBABILITY_FAILURE, PACKET_SIZE, GUARD_TIME, PACKET_RECEIVED_PROBABILITY, RECEIVER_NOT_IN_CHANNEL)
    print(f"Transmission time for Projected DAO Draft: {time_route2:.2f} ms")

    time_route3, _ = calculate_transmission_time(4, CCA, CCA_PROBABILITY_FAILURE, PACKET_SIZE, GUARD_TIME, PACKET_RECEIVED_PROBABILITY, RECEIVER_NOT_IN_CHANNEL)
    print(f"Transmission time for Projected DAO Draft and RPL Multicast: {time_route3:.2f} ms")
