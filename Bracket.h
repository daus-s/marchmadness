#ifndef BRACKET_H
#define BRACKET_H

#include "Game.h"
#include <string>
#include <array>

class Bracket {
public:
    Bracket(int year, std::array<Game, 63> games);
    int getYear() const;
    std::array<Game, 63> getGames() const;
private:
    int year;
    std::array<Game, 63> games;
};

#endif