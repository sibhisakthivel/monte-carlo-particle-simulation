//To do:
//Create particle class w/ constructor and a method to move the particle
//Create Lennard Jones class that computes the LJ potential, total energy of
//the system and show positions of all particles

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <vector>
#include "matplotlibcpp.h" //plotting
#include <filesystem> //handle output folder

namespace plt = matplotlibcpp;
namespace outpath = std::filesystem;

const double sim_size = 100;
const int numparticles = 200;
const int steps = 10000;
const double displacement = 0.03;
const double a = 1;
const double b = 1;
const double temp = 37;

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
        double r6 = std::pow(r, 6);
        double r3 = std::pow(r, 3);
        return (a / r6) - (b / r3);
    }

    //to find the max potential energy of the system
    double potential_energy() const {
        double e = 0;
        for (int i = 0; i < (int)particles.size(); i++) {
            for (int j = i + 1; j < (int)particles.size(); j++){
                double dx = particles[i].x - particles[j].x;
                double dy = particles[i].y - particles[j].y;
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

//save a plot for the current particle positions
void save_iter_plot(const std::vector<particle> &pts,
                    int step,
                    const std::string &prefix = "lennardjones_step_")
{

    //link output folder
    const std::string folder = "out";
    outpath::create_directories(folder);

    //current coordinates
    std::vector<double> x, y;
    x.reserve(pts.size());
    y.reserve(pts.size());
    for (const auto &k : pts)
    {
        x.push_back(k.x);
        y.push_back(k.y);
    }

    plt::clf(); //clear previous frame
    plt::figure_size(250, 250);
    plt::scatter(x, y, 10);
    plt::xlim(0.0, sim_size);
    plt::ylim(0.0, sim_size);
    plt::title("Lennard Jones step " + std::to_string(step));
    plt::xlabel("x");
    plt::ylabel("y");

    char fname[256];
    std::snprintf(fname, sizeof(fname), "%s/%s%04d.png", folder.c_str(), prefix.c_str(), step);
    plt::save(fname);
}

int main() {
    lennard_jones system (numparticles);
    std::cout << "initial positions:" << std::endl;
    system.printpos();
    std::cout << std::endl;
    save_iter_plot(system.particles, 0); //initial particle position plot

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

        //plot every 1000th iteration
        if (step == 0 || (step + 1) % 1000 == 0 || step == steps - 1)
        {
            save_iter_plot(system.particles, step + 1);
        }
    }
    
    std::cout << "ending positions: " << std::endl;
    system.printpos();
    return 0;
}