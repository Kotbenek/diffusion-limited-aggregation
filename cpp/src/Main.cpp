#include "Main.h"

#include <iostream>
#include <fstream>
#include <random>

std::random_device rd;
std::mt19937 e(rd());
std::uniform_real_distribution<> d_x(START_X, STOP_X);
std::uniform_real_distribution<> d_y(START_Y, STOP_Y);
std::uniform_real_distribution<> d_i(-ION_MOVEMENT, ION_MOVEMENT);

void move(float X[], float Y[], bool active[])
{
    for (int i = 0; i < ION_COUNT; i++)
    {
        if (active[i])
        {
            X[i] += d_i(e);
            Y[i] += d_i(e);

            if (X[i] < START_X)
                X[i] = START_X;
            if (X[i] > STOP_X)
                X[i] = STOP_X;
            if (Y[i] < START_Y)
                Y[i] = START_Y;
            if (Y[i] > STOP_Y)
                Y[i] = STOP_Y;
        }
    }
}

void write_to_file(float X1, float Y1, float X2, float Y2)
{
    std::ofstream f;
    f.open("tree_connections.txt", std::ios_base::app);
    f << X1 << " " << Y1 << " " << X2 << " " << Y2 << "\n";
    f.close();
}

void collide(float X[], float Y[], bool active[])
{
    for (int i = 0; i < ION_COUNT; i++)
    {
        for (int j = 0; j < ION_COUNT; j++)
        {
            if (i == j)
                continue;
            if (active[i])
                break;
            if (!active[j])
                continue;

            float distance = sqrt(pow(X[i] - X[j], 2) + pow(Y[i] - Y[j], 2));
            if (distance <= 2 * ION_RADIUS)
            {
                active[j] = false;
                write_to_file(X[i], Y[i], X[j], Y[j]);
            }
        }
    }
}

int active_count(bool active[])
{
    int c = 0;
    for (int i = 0; i < ION_COUNT; i++)
        if (active[i])
            c++;
    return c;
}

int main(int argc, char** argv)
{
    float X[ION_COUNT];
    float Y[ION_COUNT];
    bool active[ION_COUNT];

    for (int i = 0; i < ION_COUNT; i++)
    {
        X[i] = d_x(e);
        Y[i] = d_y(e);
        active[i] = true;
    }

    //Tree starting point
    active[0] = false;
    X[0] = (STOP_X - START_X) / 2;
    Y[0] = (STOP_Y - START_Y) / 2;

    int count;

    while(1)
    {
        move(X, Y, active);
        collide(X, Y, active);
        count = active_count(active);
        std::cout << count << "\n";
        if (count == 0)
            break;
    }

    return 0;
}
