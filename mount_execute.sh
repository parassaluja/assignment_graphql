wget https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb
sudo su azureuser dpkg -i /home/azureuser/packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install blobfuse fuse
mkdir -p /home/azureuser/blobcache
mkdir -p /home/azureuser/databricks
sudo chown azureuser /home/azureuser/blobcache
sudo chown azureuser /home/azureuser/databricks
blobfuse /home/azureuser/databricks --tmp-path=/home/azureuser/blobcache -o attr_timeout=240 -o entry_timeout=240 -o negative_timeout=120 --config-file=/home/azureuser/connection.cfg --log-level=LOG_DEBUG --file-cache-timeout-in-seconds=120
