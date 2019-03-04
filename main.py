from .argparser import build_parser


def main():
    parser = build_parser()
    args = parser.parse_args()
