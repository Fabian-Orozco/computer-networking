// C++ UDP Receiver

#include "Network.h"
#include <iostream>

#pragma once

int main() {
  int PORT = 8888;

  try {
    WSASession Session;
    UDPSocket Socket;
    char buffer[100];

    Socket.Bind(PORT);
    while (true) {
      sockaddr_in add = Socket.RecvFrom(buffer, sizeof(buffer));
      std::string input(buffer);
      std::cout << "Data received: " << input << std::endl;
    }
  }
  catch (std::system_error& e) {
    std::cout << e.what();
  }
}