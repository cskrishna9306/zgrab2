# open -a Docker

# docker run --rm -i -v /Users/saaiii/Desktop/code/S3-ACL-Scanner/config.ini:/config.ini ghcr.io/zmap/zgrab2 multiple -c /config.ini
./zgrab2 http --endpoint=/acl -o output.txt -f domains-only.txt --senders=500 --timeout=10 --retry-https --gomaxprocs=4 --redirects-succeed --max-redirects=5