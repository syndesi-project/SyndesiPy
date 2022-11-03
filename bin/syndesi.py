#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='syndesi',
        description='description'
    )
    parser.add_argument('-i', '--id', help='SyndesiID : "192.168.1.12" or "COM4" or "ttyUSB0"') # Syndesi ID
    parser.add_argument('-c', '--count')
    parser.add_argument('payload_parameters', metavar='Payload parameters', type=str, nargs='+',
                    help='Parameters in the form xxx=123')


    args = parser.parse_args()

    print(args.count, args.integers)

if __name__ == '__main__':
    main()
