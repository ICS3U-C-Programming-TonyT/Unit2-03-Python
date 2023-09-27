#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Sept. 26, 2023
# Get's users radius then calculates the Circumference.
import constants


def main():
    TAU = constants.TAU
    radius = float(input("Radius: "))
    circumference = round(float(format(TAU * radius)), 2)
    print(f"Circumference [ {TAU} * {radius} = {circumference} ]")


if __name__ == "__main__":
    main()
