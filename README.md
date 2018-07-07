# Holistic Composer

Holistic Composer is a framework for composing and managing the lifecycle of SFCs formed by VNFs built with Click-on-OSv. We call the proposed  approach *holistic* as it defines a generic API for the composition of SFCs that leverages particular details of different NFV orchestrators. This framework was specified according to the ETSI NFV-MANO architecture and aims simplifying the composition and lifecycle management of VNF service chains on multiple NFV platforms. Multiple SFC compositions can be done concurrently. Currently, the Holistic Composer framework works with the OpenStack Tacker NFV orchestrator. In addition, we are implementing a communication agent for the OSM Orchestrator. Other NFV platforms such as Open Baton are also planned to work with.

## Prerequisites

Holistic Composer has the following software prerequisites:

* [OpenStack](https://www.openstack.org/) - OpenStack/Pike
* [Tacker](https://wiki.openstack.org/wiki/Tacker) - Tacker/Pike
* [Click-on-OSv](https://github.com/lmarcuzzo/click-on-osv) - Click-on-OSv
* [MongoDB](https://www.mongodb.com/) - Database
* [Memcached](https://memcached.org/) - Distributed Memory Object Caching System
* [Apache](https://httpd.apache.org/) - HTTP Server (*Optional*)

## Installing

* OpenStack and Tacker can be installed via *devstack*. The implementation and testing was done using the *Pike* version.
* Default configuration for MongoDB and Memcached should work with the framework.

## Running

**Server Side**
```./core```

**Client**
```./client```

* There are a few VNF Packages in the [example](example) directory that can be used as *VNF Package* in Client Application.
* Generic VNF Packages were tested using [Xenial Ubuntu Cloud Images](https://cloud-images.ubuntu.com/xenial/)

*PS: Use relative path on informing the VNF Package directory location.*
*PSS: Click functions are just hypothetical examples.*

## Built With

* [Python 3](https://www.python.org/)

## Reference

Detailed information can be seen [here](http://portaldeconteudo.sbc.org.br/index.php/sbrc/article/view/2489/2453) (*in Portuguese*)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

