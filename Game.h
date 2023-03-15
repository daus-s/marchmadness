#ifndef GAME_H
#define GAME_H

#include <string>

class Game {
public:
    Game();
    Game(std::string teamA, std::string teamB, int scoreA, int scoreB);
    std::string getTeamA() const;
    std::string getTeamB() const;
    int getScoreA() const;
    int getScoreB() const;
    void setTeamA(std::string teamA);
    void setTeamB(std::string teamB);
    void setScoreA(int scoreA);
    void setScoreB(int scoreB);

private:
    std::string teamA;
    std::string teamB;
    int scoreA;
    int scoreB;
};

#endif
