#!/bin/bash


dir=$HOME/ym0_project


mkdir -p exec_broker
mkdir -p exec_raspi

ln -sfv $dir/mqtt_proxy/mqtt_proxy.py exec_broker/
ln -sfv $dir/mqtt_proxy/mqtt_proxy.sh exec_broker/
ln -sfv $dir/mqtt_proxy/tunnel.sh exec_broker/

ln -sfv $dir/object_detector/app/detector.py exec_broker/
ln -sfv $dir/object_detector/app/detector.sh exec_broker/
ln -sfv $dir/object_detector/trains .

ln -sfv $dir/theta_raspi/picture_viewer/web exec_broker/
ln -sfv $dir/theta_raspi/play_sound/play_sound.py exec_raspi/

