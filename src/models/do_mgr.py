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
import logging
from datetime import datetime
from os import getenv

import digitalocean

logger = logging.getLogger()


class DigitalOcean:
    def __init__(self):
        self.mgr = self.set_manager()

    @staticmethod
    def set_manager() -> digitalocean.Manager:
        """Open connection with DigitalOcean API."""
        try:
            return digitalocean.Manager(token=getenv("DO_TOKEN"))
        except Exception as exc:
            raise Exception("Couldn't connect with DigitalOcean.") from exc

    def volume_snapshots(self, volume_ids: list) -> None:
        """Do snapshot of selected volume ids."""
        try:
            logger.info("Backing up volumes...")
            for volume_id in volume_ids:
                volume = self.mgr.get_volume(volume_id)
                logger.info(f"Creating snapshot for volume ID {volume.id!r}...")
                snap = volume.snapshot(
                    name=f'{volume.name}-{datetime.now().strftime("%Y%m%d")}',
                )
                logger.info(
                    f"Snapshot {snap['snapshot']['name']!r} created successfully."
                )
        except Exception as exc:
            raise Exception("An error occurred backing up volumes.") from exc

    def delete_volume_snapshots(self, volume_ids: list, retention_days: int) -> None:
        """Delete old snapshots for selected volume ids."""
        try:
            logger.info("Running snapshots cleanup...")
            logger.info(f"Retention is set to {retention_days!r} days.")
            snapshots = self.mgr.get_volume_snapshots()
            for volume_id in volume_ids:
                volume = self.mgr.get_volume(volume_id)
                logger.info(f"Searching snapshots for volume {volume.name!r}...")
                for snapshot in snapshots:
                    # FIXME: There's no relation between snapshots and volumes.
                    # Snapshot name will be used to match snapshots for each volume.
                    if volume.name in snapshot.name:
                        logger.info(f"Found snapshot {snapshot.name!r}.")
                        creation_date = datetime.strptime(
                            snapshot.created_at, "%Y-%m-%dT%H:%M:%SZ"
                        )
                        logger.info(f"Snapshot creation date is {creation_date!r}.")
                        snap_days = (datetime.now() - creation_date).days
                        if snap_days > retention_days:
                            logger.info(f"Deleting snapshot {snapshot.id}...")
                            snapshot.destroy()
                        else:
                            logger.info("Snapshot will be retained.")
        except Exception as exc:
            raise Exception("An error occurred deleting old snapshots.") from exc
