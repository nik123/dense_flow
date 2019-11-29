import argparse
import os
import numpy as np

from extract_flow import FlowExtractor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', help='Path to source numpy file')
    parser.add_argument('--dst', help='Path to output numpy file')
    args = parser.parse_args()
    extractor = FlowExtractor(dev_id=0)

    if not os.path.exists(args.src):
        raise ValueError("Path doesn't exist:", args.src)

    src = np.load(args.src)

    f = FlowExtractor(dev_id=0)
    dst = f.extract_flow(src)
    np.save(args.dst, dst)


if __name__ == '__main__':
    main()
