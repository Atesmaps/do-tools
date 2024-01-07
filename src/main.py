#!/usr/bin/env python3
######################################################
#
#   ** Atesmaps Digital Ocean Tools **
#
#   An Atesmaps tool with scripts to maintain
#   infrastructure deployed in Digital Ocean cloud.
#
#   Collaborators:
#     - Nil Torrano: ntorrano@atesmaps.org
#     - Atesmaps Team: info@atesmaps.org
#
#   January 2024
#
######################################################
import argparse
import logging

from models.do_mgr import DigitalOcean

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def set_args() -> argparse:
    """Setup arguments parser."""
    parser = argparse.ArgumentParser(
        description="Digital Ocean Tools to maintain Atesmaps infrastructure."
    )
    subparsers = parser.add_subparsers(
        title="Digital Ocean Actions",
        dest="action",
        help="Select Digital Ocean action.",
    )

    # Volumes snapshots parser
    backup_volumes_parser = subparsers.add_parser(
        "volume-snapshots",
        help="Do a volume snapshots and keep until selected retention.",
    )
    backup_volumes_parser.add_argument(
        "--volume-ids",
        nargs="+",
        default=[],
        required=True,
        dest="volume_ids",
        help="The volume IDs that you want to backup.",
    )
    backup_volumes_parser.add_argument(
        "--retention-days",
        type=int,
        default=7,
        dest="retention_days",
        help="The number of days that you want to keep snapshots.",
    )

    return parser.parse_args()


def main() -> None:
    """Execute Digital Ocean Tool Script."""
    logger.info("** Atesmaps Digital Ocean Tools **")

    # Init argument parser
    args = set_args()

    do = DigitalOcean()
    if args.action == "volume-snapshots":
        logger.info("Volume Snapshots Action Selected.")
        do.volume_snapshots(volume_ids=args.volume_ids)
        do.delete_volume_snapshots(
            volume_ids=args.volume_ids,
            retention_days=args.retention_days,
        )
    else:
        logger.error(f"Action {args.action} not recognized.")

    # End
    logger.info("Process ended successfully.")


if __name__ == "__main__":
    main()
