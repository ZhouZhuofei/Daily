# Operate
##operation
***************
```shell
$ docker run -it fregot/cheers2019
```
**************
list all images in local computer
```shell
$docker images
```
*************
##operation 2
add tags for images tag
```shell
$docker tag ubuntu:latest myubuntu:latest
```
*************
see all imformation for these docker images
```shell
$ docker inspect fregot/cheers2019
```
*************
ues inspect -f to seach for detail in images content

************
docker search to find far-end images
    -  --automated=true|false: if show automated images
    -  --no-trunc=true|false: output information endless, default false
    -  -s, --stars=X:only show the images'stars over X

```shell
$ docker search --automated -s 5 ubuntu
```
***********
delete

```shell
$ docker rmi myubuntu:latest
```
force delete

```shell
$ docker rmi -f myubuntu:latest
```
********
##create

