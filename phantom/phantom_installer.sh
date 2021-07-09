#####################
#
# This script grabs a list of releases downloads/ extracts and starts the install process.
# This script has only been tested with with the 4.10.x Releases on CentOS
#
#####################

versions=$(curl https://docs.splunk.com/Documentation/Phantom/4.10.4/Install/PhantomReposAndSigningKeys#For_Splunk_Phantom_deployments_without_internet_access_or_unprivileged_deployments | grep -P "\<td\>\d\.\d*\.\d*" | awk '{FS="<.?td>"} {print $2}')

printf "\n\n"
#Printing available versions
echo 'Available versions according to https://docs.splunk.com/Documentation/Phantom/4.10.4/Install/PhantomReposAndSigningKeys#For_Splunk_Phantom_deployments_without_internet_access_or_unprivileged_deployments.'
printf "\n\n\n"

for row in $versions
do
	length=$(echo "${row##*$'\.'}"|wc -c)
	if [ $length -gt 2 ]
		then
        echo $row
	fi
done

printf '\nWhat version would like like?\n'

read -e requested
shortened=$(echo $requested | sed -E 's/\.[0-9]+$//')

printf 'installing Phantom version:'$requested'\n'
printf 'shortened version is:' $shortened '\n'

wget http://download.splunk.com/products/phantom/release/linux/$shortened/phantom_offline_setup_centos7-$requested.tgz || wget http://download.splunk.com/products/phantom/release/linux/$requested/phantom_offline_setup_centos7-$requested.tgz

tar xf ./phantom_offline_setup_centos7-$requested.tgz
cd ./phantom_offline_setup_centos7-$requested
./phantom_offline_setup_centos.sh install
cd ../

/opt/phantom/bin/stop_phantom.sh
    #### Fix for broken web service ###
setfacl -b /var/log/phantom/app_install.log;
chmod 775 /var/log/phantom/app_install.log;

/opt/phantom/bin/start_phantom.sh
rm -f phantom_offline_setup_centos7-$requested.tgz
rm -rf phantom_offline_setup_centos7-$requested
