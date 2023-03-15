Game::Game() {}

Game::Game(std::string teamA, std::string teamB, int scoreA, int scoreB) {
    this->teamA = teamA;
    this->teamB = teamB;
    this->scoreA = scoreA;
    this->scoreB = scoreB;
}

std::string Game::getTeamA() const {
    return teamA;
}

std::string Game::getTeamB() const {
    return teamB;
}

int Game::getScoreA() const {
    return scoreA;
}

int Game::getScoreB() const {
    return scoreB;
}

void Game::setTeamA(std::string teamA) {
    this->teamA = teamA;
}

void Game::setTeamB(std::string teamB) {
    this->teamB = teamB;
}
