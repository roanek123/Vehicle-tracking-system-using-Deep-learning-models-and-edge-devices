#!/bin/bash

# Infinite loop
while true; do
    # Set the duration in milliseconds
    duration=10000

    # Set the output filename
    output_file="test.h264"

    # Run the libcamera-vid command with specified options
    libcamera-vid -t $duration -o $output_file

    # Check if libcamera-vid command was successful
    if [ $? -eq 0 ]; then
        # Convert the .h264 file to .mp4 using ffmpeg
        input_file="test.h264"
        output_file="output.mp4"

        # Check if the input file exists
        if [ -f "$input_file" ]; then
            # Convert .h264 to .mp4 using ffmpeg
            ffmpeg -y -framerate 30 -i "$input_file" -c copy "$output_file"

            # Check if ffmpeg command was successful
            if [ $? -eq 0 ]; then
                echo "Conversion completed successfully."
            else
                echo "Error: Conversion failed."
            fi
        else
            echo "Error: Input file $input_file not found."
        fi
    else
        echo "Error: libcamera-vid command failed."
    fi

    # Wait for one minute before running the commands again
    sleep 60
done