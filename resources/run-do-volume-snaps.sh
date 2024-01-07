#!/bin/bash
#########################################################
#
#    Run Atesmaps Digital Ocean Tools with volume
#    snapshots action.
#
#    Remember to setup log rotation!
#
#    Collaborators:
#     * Nil Torrano: <ntorrano@atesmaps.org>
#     * Atesmaps Team: <info@atesmaps.org>
#
#    January 2024
#
#########################################################

# Log filename
LOG_FILE=/var/log/atesmaps-do-tools/volume-snapshots/atesmaps_do_volume_snaps.log

# Set log trace
echo -e "\n\n########### Atesaps DigitalOcean Tool - Volume Snapshots - $(date +%Y-%m-%d) $(date +%H:%M:%S) ###########" >> ${LOG_FILE}

# Run docker image
docker run \
	-e "DO_TOKEN=<your-digitalocean-token>" \
	--rm \
	--name atesmaps-do-tools \
	atesmaps-do-tools:latest \
	volume-snapshots \
	--volume-ids \
	  3f17cbe1-4300-11ed-865c-0a58ac1482e9 \
	>> ${LOG_FILE} 2>&1

# End log trace
echo -e "\n\n#########################################################################" >> ${LOG_FILE}

exit 0
