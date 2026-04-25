#include <chrono>

#include "matrix.hpp"

int main()
{
    try
    {
        Matrix<int> A(PROJECT_ROOT "/input/A.csv");
        Matrix<int> B(PROJECT_ROOT "/input/B.csv");

        auto start = std::chrono::high_resolution_clock::now();
        Matrix<int> C = A * B;
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);

        std::string outpath = PROJECT_ROOT "/output/C.txt";
        std::ofstream file(outpath);
        if (!file.is_open()) throw std::runtime_error("Could not open output file!");
        file << C.rows() << " " << C.cols() << "\n";
        file << C << "\n";
        file << "Time: " << duration.count() << " microseconds\n\n";
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
