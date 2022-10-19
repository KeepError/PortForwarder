# Port forwarder

Python app that allows forward local ports to remote server

## Deploy

### Config

Rename [.config-example](https://github.com/KeepError/PortForwarder/blob/master/.config-example) to `.config` and edit
it.

### Docker

To run use Docker:

```bash
docker-compose build
docker-compose -d up
docker-compose ps
```