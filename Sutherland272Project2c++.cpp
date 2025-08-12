//To do:
//Create particle class w/ constructor and a method to move the particle
//Create Lennard Jones class that computes the LJ potential, total energy of
//the system and show positions of all particles

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <vector>
#include "matplotlibcpp.h"
namespace plt = matplotlibcpp;

const double sim_size = 25;
const int numparticles = 5;
const int steps = 100;
const double displacement = 0.3;
const double epsilon = 1;
const double sigma = 1;
const double temp = 1;

class particle {
public: //to make easily accessible throughout the rest of the code
    double x;
    double y;

    //create constructor
    particle() {
        x = ((double)std::rand() / RAND_MAX) * sim_size;
        y = ((double)std::rand() / RAND_MAX) * sim_size;
    }

    //cause particles to move randomly
    void move() {
        x += ((double)std::rand() / RAND_MAX * 2 - 1) * displacement;
        y += ((double)std::rand() / RAND_MAX * 2 - 1) * displacement;

        // to keep particles in sim boundaries
        if (x < 0) x += sim_size;
        if (x >= sim_size) x -= sim_size;
        if (y < 0) y += sim_size;
        if (y >= sim_size) y -= sim_size;
    }
};

class lennard_jones {
    public:
    std::vector<particle> particles;
    //implementing N amount of random particles
    lennard_jones(int N) : particles (N){}
    //Lennard_Jones potential using Euclidean distance formula
    double l_j (double dx, double dy) const {
        //have to use r2 and r6 bc r**2 (etc.) is invalid for c++
        double r = std::sqrt (dx * dx + dy * dy);
        //to prevent division by zero
        if (r == 0) return 0;
        double r6 = std::pow(sigma / r, 6);
        double r12 = std::pow(sigma / r, 12);
        return 4 * epsilon * (r12 - r6);
    }

    //to find the max potential energy of the system
    double potential_energy() const {
        double e = 0;
        for (int i = 0; i < (int)particles.size(); i++) {
            for (int j = i + 1; j < (int)particles.size(); j++){
                double dx = particles[i].x - particles[j].x;
                double dy = particles[i].y - particles[j].y;

                //using MIC to ensure correct distance between particles
                //is being measured
                if (dx > sim_size / 2) dx -= sim_size;
                if (dx < -sim_size / 2) dx += sim_size;
                if (dy > sim_size / 2) dy -= sim_size;
                if (dy < -sim_size / 2) dy += sim_size;

                e += l_j(dx, dy);
            }
        }
        return e;
    }

    void printpos() {
        for (int i = 0; i < (int)particles.size(); i++) {
            std::cout << "particle " << i << ": " << particles[i].x << " "
            << particles[i].y << std::endl;
        }
    }
};

int main() {
    lennard_jones system (numparticles);
    std::cout << "initial positions:" << std::endl;
    system.printpos();
    std::cout << std::endl;

    //initial plot
    {std::vector<double> x, y;
    x.reserve(system.particles.size());
    y.reserve(system.particles.size());
    for (const auto& k : system.particles) {x.push_back(k.x); y.push_back(k.y);}

    plt::plot(x, y);
    plt::figure_size(250,250);
    plt::scatter(x, y, 10);
    plt::title("Lennard Jones Initial");
    plt::xlabel("x");
    plt::ylabel("y");
    plt::save("lennardjonesinitial.png");
}

    //Metropolis loop
    for (int step = 0; step < steps; step++) {
        int i = std::rand() % numparticles;

        double old_x = system.particles[i].x;
        double old_y = system.particles[i].y;
        double old_energy = system.potential_energy();

        system.particles[i].move();

        double new_energy = system.potential_energy();
        double deltaE = new_energy - old_energy;
        if (deltaE > 0) {
            double r = (double)std::rand() / RAND_MAX;
            if (r > std::exp(-deltaE / temp)) {
                system.particles[i].x = old_x;
                system.particles[i].y = old_y;
            }
        }
    }
    
    std::cout << "ending positions: " << std::endl;
    system.printpos();

    #final plot
    {std::vector<double> x, y;
    x.reserve(system.particles.size());
    y.reserve(system.particles.size());
    for (const auto& k : system.particles) {x.push_back(k.x); y.push_back(k.y);}

    plt::plot(x, y);
    plt::figure_size(250,250);
    plt::scatter(x, y, 10);
    plt::title("Lennard Jones Final");
    plt::xlabel("x");
    plt::ylabel("y");
    plt::save("lennardjonesfinal.png");
    }
    return 0;

}