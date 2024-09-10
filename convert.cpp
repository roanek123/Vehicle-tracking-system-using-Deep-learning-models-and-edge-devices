#include <iostream>
#include <cstdlib>

int main() {
    const char* input_file = "test.h264";
    const char* output_file = "test.mp4";

    // Construct FFmpeg command to convert H.264 to MP4
    std::string command = "ffmpeg -i " + std::string(input_file) + " -c:v copy -c:a aac -strict experimental " + std::string(output_file);

    // Execute FFmpeg command
    int status = std::system(command.c_str());

    if (status == 0) {
        std::cout << "File '" << input_file << "' converted to '" << output_file << "' successfully!" << std::endl;
    } else {
        std::cerr << "Error occurred during conversion." << std::endl;
    }

    return 0;
}
