# zschema sub-schema for zgrab2's mongodb module
# Registers zgrab2-mongodb globally, and mongodb with the main zgrab2 schema.
from zschema.leaves import *
from zschema.compounds import *
import zschema.registry

import zcrypto_schemas.zcrypto as zcrypto
import zgrab2

mongodb_scan_response = SubRecord({
    "result": SubRecord({
        "version": String(doc="Version of mongodb server"),
        "git_version": String(doc="Git Version of mongodb server"),
        "build_environment": SubRecord({
            "dist_mod": String(),
            "dist_arch": String(),
            "cc": String(),
            "cc_flags": String(),
            "cxx": String(),
            "cxx_flags": String(),
            "link_flags": String(),
            "target_arch": String(),
            "target_os": String()})
    })
}, extends=zgrab2.base_scan_response)

zschema.registry.register_schema("zgrab2-mongodb", mongodb_scan_response)

zgrab2.register_scan_response_type("mongodb", mongodb_scan_response)
