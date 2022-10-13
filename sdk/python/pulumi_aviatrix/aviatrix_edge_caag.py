# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AviatrixEdgeCaagArgs', 'AviatrixEdgeCaag']

@pulumi.input_type
class AviatrixEdgeCaagArgs:
    def __init__(__self__, *,
                 lan_interface_ip_prefix: pulumi.Input[str],
                 management_interface_config: pulumi.Input[str],
                 wan_default_gateway_ip: pulumi.Input[str],
                 wan_interface_ip_prefix: pulumi.Input[str],
                 ztp_file_download_path: pulumi.Input[str],
                 ztp_file_type: pulumi.Input[str],
                 dns_server_ip: Optional[pulumi.Input[str]] = None,
                 enable_over_private_network: Optional[pulumi.Input[bool]] = None,
                 local_as_number: Optional[pulumi.Input[str]] = None,
                 management_default_gateway_ip: Optional[pulumi.Input[str]] = None,
                 management_egress_ip_prefix: Optional[pulumi.Input[str]] = None,
                 management_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 prepend_as_paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secondary_dns_server_ip: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AviatrixEdgeCaag resource.
        :param pulumi.Input[str] lan_interface_ip_prefix: LAN interface IP / prefix.
        :param pulumi.Input[str] management_interface_config: Management interface configuration. Valid values: 'DHCP' and 'Static'.
        :param pulumi.Input[str] wan_default_gateway_ip: WAN default gateway IP.
        :param pulumi.Input[str] wan_interface_ip_prefix: WAN interface IP / prefix.
        :param pulumi.Input[str] ztp_file_download_path: The location where the Edge as a CaaG ZTP file will be stored.
        :param pulumi.Input[str] ztp_file_type: ZTP file type.
        :param pulumi.Input[str] dns_server_ip: DNS server IP.
        :param pulumi.Input[bool] enable_over_private_network: Enable management over private network.
        :param pulumi.Input[str] local_as_number: Local AS number.
        :param pulumi.Input[str] management_default_gateway_ip: Management default gateway IP.
        :param pulumi.Input[str] management_egress_ip_prefix: Management egress gateway IP / prefix.
        :param pulumi.Input[str] management_interface_ip_prefix: Management interface IP / prefix.
        :param pulumi.Input[str] name: Edge as a CaaG name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] prepend_as_paths: AS path prepend.
        :param pulumi.Input[str] secondary_dns_server_ip: Secondary DNS server IP.
        """
        pulumi.set(__self__, "lan_interface_ip_prefix", lan_interface_ip_prefix)
        pulumi.set(__self__, "management_interface_config", management_interface_config)
        pulumi.set(__self__, "wan_default_gateway_ip", wan_default_gateway_ip)
        pulumi.set(__self__, "wan_interface_ip_prefix", wan_interface_ip_prefix)
        pulumi.set(__self__, "ztp_file_download_path", ztp_file_download_path)
        pulumi.set(__self__, "ztp_file_type", ztp_file_type)
        if dns_server_ip is not None:
            pulumi.set(__self__, "dns_server_ip", dns_server_ip)
        if enable_over_private_network is not None:
            pulumi.set(__self__, "enable_over_private_network", enable_over_private_network)
        if local_as_number is not None:
            pulumi.set(__self__, "local_as_number", local_as_number)
        if management_default_gateway_ip is not None:
            pulumi.set(__self__, "management_default_gateway_ip", management_default_gateway_ip)
        if management_egress_ip_prefix is not None:
            pulumi.set(__self__, "management_egress_ip_prefix", management_egress_ip_prefix)
        if management_interface_ip_prefix is not None:
            pulumi.set(__self__, "management_interface_ip_prefix", management_interface_ip_prefix)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if prepend_as_paths is not None:
            pulumi.set(__self__, "prepend_as_paths", prepend_as_paths)
        if secondary_dns_server_ip is not None:
            pulumi.set(__self__, "secondary_dns_server_ip", secondary_dns_server_ip)

    @property
    @pulumi.getter(name="lanInterfaceIpPrefix")
    def lan_interface_ip_prefix(self) -> pulumi.Input[str]:
        """
        LAN interface IP / prefix.
        """
        return pulumi.get(self, "lan_interface_ip_prefix")

    @lan_interface_ip_prefix.setter
    def lan_interface_ip_prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "lan_interface_ip_prefix", value)

    @property
    @pulumi.getter(name="managementInterfaceConfig")
    def management_interface_config(self) -> pulumi.Input[str]:
        """
        Management interface configuration. Valid values: 'DHCP' and 'Static'.
        """
        return pulumi.get(self, "management_interface_config")

    @management_interface_config.setter
    def management_interface_config(self, value: pulumi.Input[str]):
        pulumi.set(self, "management_interface_config", value)

    @property
    @pulumi.getter(name="wanDefaultGatewayIp")
    def wan_default_gateway_ip(self) -> pulumi.Input[str]:
        """
        WAN default gateway IP.
        """
        return pulumi.get(self, "wan_default_gateway_ip")

    @wan_default_gateway_ip.setter
    def wan_default_gateway_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "wan_default_gateway_ip", value)

    @property
    @pulumi.getter(name="wanInterfaceIpPrefix")
    def wan_interface_ip_prefix(self) -> pulumi.Input[str]:
        """
        WAN interface IP / prefix.
        """
        return pulumi.get(self, "wan_interface_ip_prefix")

    @wan_interface_ip_prefix.setter
    def wan_interface_ip_prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "wan_interface_ip_prefix", value)

    @property
    @pulumi.getter(name="ztpFileDownloadPath")
    def ztp_file_download_path(self) -> pulumi.Input[str]:
        """
        The location where the Edge as a CaaG ZTP file will be stored.
        """
        return pulumi.get(self, "ztp_file_download_path")

    @ztp_file_download_path.setter
    def ztp_file_download_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "ztp_file_download_path", value)

    @property
    @pulumi.getter(name="ztpFileType")
    def ztp_file_type(self) -> pulumi.Input[str]:
        """
        ZTP file type.
        """
        return pulumi.get(self, "ztp_file_type")

    @ztp_file_type.setter
    def ztp_file_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "ztp_file_type", value)

    @property
    @pulumi.getter(name="dnsServerIp")
    def dns_server_ip(self) -> Optional[pulumi.Input[str]]:
        """
        DNS server IP.
        """
        return pulumi.get(self, "dns_server_ip")

    @dns_server_ip.setter
    def dns_server_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_server_ip", value)

    @property
    @pulumi.getter(name="enableOverPrivateNetwork")
    def enable_over_private_network(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable management over private network.
        """
        return pulumi.get(self, "enable_over_private_network")

    @enable_over_private_network.setter
    def enable_over_private_network(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_over_private_network", value)

    @property
    @pulumi.getter(name="localAsNumber")
    def local_as_number(self) -> Optional[pulumi.Input[str]]:
        """
        Local AS number.
        """
        return pulumi.get(self, "local_as_number")

    @local_as_number.setter
    def local_as_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "local_as_number", value)

    @property
    @pulumi.getter(name="managementDefaultGatewayIp")
    def management_default_gateway_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Management default gateway IP.
        """
        return pulumi.get(self, "management_default_gateway_ip")

    @management_default_gateway_ip.setter
    def management_default_gateway_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_default_gateway_ip", value)

    @property
    @pulumi.getter(name="managementEgressIpPrefix")
    def management_egress_ip_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Management egress gateway IP / prefix.
        """
        return pulumi.get(self, "management_egress_ip_prefix")

    @management_egress_ip_prefix.setter
    def management_egress_ip_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_egress_ip_prefix", value)

    @property
    @pulumi.getter(name="managementInterfaceIpPrefix")
    def management_interface_ip_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Management interface IP / prefix.
        """
        return pulumi.get(self, "management_interface_ip_prefix")

    @management_interface_ip_prefix.setter
    def management_interface_ip_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_interface_ip_prefix", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Edge as a CaaG name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="prependAsPaths")
    def prepend_as_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        AS path prepend.
        """
        return pulumi.get(self, "prepend_as_paths")

    @prepend_as_paths.setter
    def prepend_as_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "prepend_as_paths", value)

    @property
    @pulumi.getter(name="secondaryDnsServerIp")
    def secondary_dns_server_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Secondary DNS server IP.
        """
        return pulumi.get(self, "secondary_dns_server_ip")

    @secondary_dns_server_ip.setter
    def secondary_dns_server_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_dns_server_ip", value)


@pulumi.input_type
class _AviatrixEdgeCaagState:
    def __init__(__self__, *,
                 dns_server_ip: Optional[pulumi.Input[str]] = None,
                 enable_over_private_network: Optional[pulumi.Input[bool]] = None,
                 lan_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
                 local_as_number: Optional[pulumi.Input[str]] = None,
                 management_default_gateway_ip: Optional[pulumi.Input[str]] = None,
                 management_egress_ip_prefix: Optional[pulumi.Input[str]] = None,
                 management_interface_config: Optional[pulumi.Input[str]] = None,
                 management_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 prepend_as_paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secondary_dns_server_ip: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 wan_default_gateway_ip: Optional[pulumi.Input[str]] = None,
                 wan_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
                 ztp_file_download_path: Optional[pulumi.Input[str]] = None,
                 ztp_file_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AviatrixEdgeCaag resources.
        :param pulumi.Input[str] dns_server_ip: DNS server IP.
        :param pulumi.Input[bool] enable_over_private_network: Enable management over private network.
        :param pulumi.Input[str] lan_interface_ip_prefix: LAN interface IP / prefix.
        :param pulumi.Input[str] local_as_number: Local AS number.
        :param pulumi.Input[str] management_default_gateway_ip: Management default gateway IP.
        :param pulumi.Input[str] management_egress_ip_prefix: Management egress gateway IP / prefix.
        :param pulumi.Input[str] management_interface_config: Management interface configuration. Valid values: 'DHCP' and 'Static'.
        :param pulumi.Input[str] management_interface_ip_prefix: Management interface IP / prefix.
        :param pulumi.Input[str] name: Edge as a CaaG name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] prepend_as_paths: AS path prepend.
        :param pulumi.Input[str] secondary_dns_server_ip: Secondary DNS server IP.
        :param pulumi.Input[str] state: State of Edge as a CaaG.
        :param pulumi.Input[str] wan_default_gateway_ip: WAN default gateway IP.
        :param pulumi.Input[str] wan_interface_ip_prefix: WAN interface IP / prefix.
        :param pulumi.Input[str] ztp_file_download_path: The location where the Edge as a CaaG ZTP file will be stored.
        :param pulumi.Input[str] ztp_file_type: ZTP file type.
        """
        if dns_server_ip is not None:
            pulumi.set(__self__, "dns_server_ip", dns_server_ip)
        if enable_over_private_network is not None:
            pulumi.set(__self__, "enable_over_private_network", enable_over_private_network)
        if lan_interface_ip_prefix is not None:
            pulumi.set(__self__, "lan_interface_ip_prefix", lan_interface_ip_prefix)
        if local_as_number is not None:
            pulumi.set(__self__, "local_as_number", local_as_number)
        if management_default_gateway_ip is not None:
            pulumi.set(__self__, "management_default_gateway_ip", management_default_gateway_ip)
        if management_egress_ip_prefix is not None:
            pulumi.set(__self__, "management_egress_ip_prefix", management_egress_ip_prefix)
        if management_interface_config is not None:
            pulumi.set(__self__, "management_interface_config", management_interface_config)
        if management_interface_ip_prefix is not None:
            pulumi.set(__self__, "management_interface_ip_prefix", management_interface_ip_prefix)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if prepend_as_paths is not None:
            pulumi.set(__self__, "prepend_as_paths", prepend_as_paths)
        if secondary_dns_server_ip is not None:
            pulumi.set(__self__, "secondary_dns_server_ip", secondary_dns_server_ip)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if wan_default_gateway_ip is not None:
            pulumi.set(__self__, "wan_default_gateway_ip", wan_default_gateway_ip)
        if wan_interface_ip_prefix is not None:
            pulumi.set(__self__, "wan_interface_ip_prefix", wan_interface_ip_prefix)
        if ztp_file_download_path is not None:
            pulumi.set(__self__, "ztp_file_download_path", ztp_file_download_path)
        if ztp_file_type is not None:
            pulumi.set(__self__, "ztp_file_type", ztp_file_type)

    @property
    @pulumi.getter(name="dnsServerIp")
    def dns_server_ip(self) -> Optional[pulumi.Input[str]]:
        """
        DNS server IP.
        """
        return pulumi.get(self, "dns_server_ip")

    @dns_server_ip.setter
    def dns_server_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_server_ip", value)

    @property
    @pulumi.getter(name="enableOverPrivateNetwork")
    def enable_over_private_network(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable management over private network.
        """
        return pulumi.get(self, "enable_over_private_network")

    @enable_over_private_network.setter
    def enable_over_private_network(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_over_private_network", value)

    @property
    @pulumi.getter(name="lanInterfaceIpPrefix")
    def lan_interface_ip_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        LAN interface IP / prefix.
        """
        return pulumi.get(self, "lan_interface_ip_prefix")

    @lan_interface_ip_prefix.setter
    def lan_interface_ip_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lan_interface_ip_prefix", value)

    @property
    @pulumi.getter(name="localAsNumber")
    def local_as_number(self) -> Optional[pulumi.Input[str]]:
        """
        Local AS number.
        """
        return pulumi.get(self, "local_as_number")

    @local_as_number.setter
    def local_as_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "local_as_number", value)

    @property
    @pulumi.getter(name="managementDefaultGatewayIp")
    def management_default_gateway_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Management default gateway IP.
        """
        return pulumi.get(self, "management_default_gateway_ip")

    @management_default_gateway_ip.setter
    def management_default_gateway_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_default_gateway_ip", value)

    @property
    @pulumi.getter(name="managementEgressIpPrefix")
    def management_egress_ip_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Management egress gateway IP / prefix.
        """
        return pulumi.get(self, "management_egress_ip_prefix")

    @management_egress_ip_prefix.setter
    def management_egress_ip_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_egress_ip_prefix", value)

    @property
    @pulumi.getter(name="managementInterfaceConfig")
    def management_interface_config(self) -> Optional[pulumi.Input[str]]:
        """
        Management interface configuration. Valid values: 'DHCP' and 'Static'.
        """
        return pulumi.get(self, "management_interface_config")

    @management_interface_config.setter
    def management_interface_config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_interface_config", value)

    @property
    @pulumi.getter(name="managementInterfaceIpPrefix")
    def management_interface_ip_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Management interface IP / prefix.
        """
        return pulumi.get(self, "management_interface_ip_prefix")

    @management_interface_ip_prefix.setter
    def management_interface_ip_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_interface_ip_prefix", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Edge as a CaaG name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="prependAsPaths")
    def prepend_as_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        AS path prepend.
        """
        return pulumi.get(self, "prepend_as_paths")

    @prepend_as_paths.setter
    def prepend_as_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "prepend_as_paths", value)

    @property
    @pulumi.getter(name="secondaryDnsServerIp")
    def secondary_dns_server_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Secondary DNS server IP.
        """
        return pulumi.get(self, "secondary_dns_server_ip")

    @secondary_dns_server_ip.setter
    def secondary_dns_server_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_dns_server_ip", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of Edge as a CaaG.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="wanDefaultGatewayIp")
    def wan_default_gateway_ip(self) -> Optional[pulumi.Input[str]]:
        """
        WAN default gateway IP.
        """
        return pulumi.get(self, "wan_default_gateway_ip")

    @wan_default_gateway_ip.setter
    def wan_default_gateway_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "wan_default_gateway_ip", value)

    @property
    @pulumi.getter(name="wanInterfaceIpPrefix")
    def wan_interface_ip_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        WAN interface IP / prefix.
        """
        return pulumi.get(self, "wan_interface_ip_prefix")

    @wan_interface_ip_prefix.setter
    def wan_interface_ip_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "wan_interface_ip_prefix", value)

    @property
    @pulumi.getter(name="ztpFileDownloadPath")
    def ztp_file_download_path(self) -> Optional[pulumi.Input[str]]:
        """
        The location where the Edge as a CaaG ZTP file will be stored.
        """
        return pulumi.get(self, "ztp_file_download_path")

    @ztp_file_download_path.setter
    def ztp_file_download_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ztp_file_download_path", value)

    @property
    @pulumi.getter(name="ztpFileType")
    def ztp_file_type(self) -> Optional[pulumi.Input[str]]:
        """
        ZTP file type.
        """
        return pulumi.get(self, "ztp_file_type")

    @ztp_file_type.setter
    def ztp_file_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ztp_file_type", value)


class AviatrixEdgeCaag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_server_ip: Optional[pulumi.Input[str]] = None,
                 enable_over_private_network: Optional[pulumi.Input[bool]] = None,
                 lan_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
                 local_as_number: Optional[pulumi.Input[str]] = None,
                 management_default_gateway_ip: Optional[pulumi.Input[str]] = None,
                 management_egress_ip_prefix: Optional[pulumi.Input[str]] = None,
                 management_interface_config: Optional[pulumi.Input[str]] = None,
                 management_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 prepend_as_paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secondary_dns_server_ip: Optional[pulumi.Input[str]] = None,
                 wan_default_gateway_ip: Optional[pulumi.Input[str]] = None,
                 wan_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
                 ztp_file_download_path: Optional[pulumi.Input[str]] = None,
                 ztp_file_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AviatrixEdgeCaag resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dns_server_ip: DNS server IP.
        :param pulumi.Input[bool] enable_over_private_network: Enable management over private network.
        :param pulumi.Input[str] lan_interface_ip_prefix: LAN interface IP / prefix.
        :param pulumi.Input[str] local_as_number: Local AS number.
        :param pulumi.Input[str] management_default_gateway_ip: Management default gateway IP.
        :param pulumi.Input[str] management_egress_ip_prefix: Management egress gateway IP / prefix.
        :param pulumi.Input[str] management_interface_config: Management interface configuration. Valid values: 'DHCP' and 'Static'.
        :param pulumi.Input[str] management_interface_ip_prefix: Management interface IP / prefix.
        :param pulumi.Input[str] name: Edge as a CaaG name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] prepend_as_paths: AS path prepend.
        :param pulumi.Input[str] secondary_dns_server_ip: Secondary DNS server IP.
        :param pulumi.Input[str] wan_default_gateway_ip: WAN default gateway IP.
        :param pulumi.Input[str] wan_interface_ip_prefix: WAN interface IP / prefix.
        :param pulumi.Input[str] ztp_file_download_path: The location where the Edge as a CaaG ZTP file will be stored.
        :param pulumi.Input[str] ztp_file_type: ZTP file type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AviatrixEdgeCaagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AviatrixEdgeCaag resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AviatrixEdgeCaagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AviatrixEdgeCaagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_server_ip: Optional[pulumi.Input[str]] = None,
                 enable_over_private_network: Optional[pulumi.Input[bool]] = None,
                 lan_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
                 local_as_number: Optional[pulumi.Input[str]] = None,
                 management_default_gateway_ip: Optional[pulumi.Input[str]] = None,
                 management_egress_ip_prefix: Optional[pulumi.Input[str]] = None,
                 management_interface_config: Optional[pulumi.Input[str]] = None,
                 management_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 prepend_as_paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secondary_dns_server_ip: Optional[pulumi.Input[str]] = None,
                 wan_default_gateway_ip: Optional[pulumi.Input[str]] = None,
                 wan_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
                 ztp_file_download_path: Optional[pulumi.Input[str]] = None,
                 ztp_file_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AviatrixEdgeCaagArgs.__new__(AviatrixEdgeCaagArgs)

            __props__.__dict__["dns_server_ip"] = dns_server_ip
            __props__.__dict__["enable_over_private_network"] = enable_over_private_network
            if lan_interface_ip_prefix is None and not opts.urn:
                raise TypeError("Missing required property 'lan_interface_ip_prefix'")
            __props__.__dict__["lan_interface_ip_prefix"] = lan_interface_ip_prefix
            __props__.__dict__["local_as_number"] = local_as_number
            __props__.__dict__["management_default_gateway_ip"] = management_default_gateway_ip
            __props__.__dict__["management_egress_ip_prefix"] = management_egress_ip_prefix
            if management_interface_config is None and not opts.urn:
                raise TypeError("Missing required property 'management_interface_config'")
            __props__.__dict__["management_interface_config"] = management_interface_config
            __props__.__dict__["management_interface_ip_prefix"] = management_interface_ip_prefix
            __props__.__dict__["name"] = name
            __props__.__dict__["prepend_as_paths"] = prepend_as_paths
            __props__.__dict__["secondary_dns_server_ip"] = secondary_dns_server_ip
            if wan_default_gateway_ip is None and not opts.urn:
                raise TypeError("Missing required property 'wan_default_gateway_ip'")
            __props__.__dict__["wan_default_gateway_ip"] = wan_default_gateway_ip
            if wan_interface_ip_prefix is None and not opts.urn:
                raise TypeError("Missing required property 'wan_interface_ip_prefix'")
            __props__.__dict__["wan_interface_ip_prefix"] = wan_interface_ip_prefix
            if ztp_file_download_path is None and not opts.urn:
                raise TypeError("Missing required property 'ztp_file_download_path'")
            __props__.__dict__["ztp_file_download_path"] = ztp_file_download_path
            if ztp_file_type is None and not opts.urn:
                raise TypeError("Missing required property 'ztp_file_type'")
            __props__.__dict__["ztp_file_type"] = ztp_file_type
            __props__.__dict__["state"] = None
        super(AviatrixEdgeCaag, __self__).__init__(
            'aviatrix:index/aviatrixEdgeCaag:AviatrixEdgeCaag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dns_server_ip: Optional[pulumi.Input[str]] = None,
            enable_over_private_network: Optional[pulumi.Input[bool]] = None,
            lan_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
            local_as_number: Optional[pulumi.Input[str]] = None,
            management_default_gateway_ip: Optional[pulumi.Input[str]] = None,
            management_egress_ip_prefix: Optional[pulumi.Input[str]] = None,
            management_interface_config: Optional[pulumi.Input[str]] = None,
            management_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            prepend_as_paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            secondary_dns_server_ip: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            wan_default_gateway_ip: Optional[pulumi.Input[str]] = None,
            wan_interface_ip_prefix: Optional[pulumi.Input[str]] = None,
            ztp_file_download_path: Optional[pulumi.Input[str]] = None,
            ztp_file_type: Optional[pulumi.Input[str]] = None) -> 'AviatrixEdgeCaag':
        """
        Get an existing AviatrixEdgeCaag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dns_server_ip: DNS server IP.
        :param pulumi.Input[bool] enable_over_private_network: Enable management over private network.
        :param pulumi.Input[str] lan_interface_ip_prefix: LAN interface IP / prefix.
        :param pulumi.Input[str] local_as_number: Local AS number.
        :param pulumi.Input[str] management_default_gateway_ip: Management default gateway IP.
        :param pulumi.Input[str] management_egress_ip_prefix: Management egress gateway IP / prefix.
        :param pulumi.Input[str] management_interface_config: Management interface configuration. Valid values: 'DHCP' and 'Static'.
        :param pulumi.Input[str] management_interface_ip_prefix: Management interface IP / prefix.
        :param pulumi.Input[str] name: Edge as a CaaG name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] prepend_as_paths: AS path prepend.
        :param pulumi.Input[str] secondary_dns_server_ip: Secondary DNS server IP.
        :param pulumi.Input[str] state: State of Edge as a CaaG.
        :param pulumi.Input[str] wan_default_gateway_ip: WAN default gateway IP.
        :param pulumi.Input[str] wan_interface_ip_prefix: WAN interface IP / prefix.
        :param pulumi.Input[str] ztp_file_download_path: The location where the Edge as a CaaG ZTP file will be stored.
        :param pulumi.Input[str] ztp_file_type: ZTP file type.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AviatrixEdgeCaagState.__new__(_AviatrixEdgeCaagState)

        __props__.__dict__["dns_server_ip"] = dns_server_ip
        __props__.__dict__["enable_over_private_network"] = enable_over_private_network
        __props__.__dict__["lan_interface_ip_prefix"] = lan_interface_ip_prefix
        __props__.__dict__["local_as_number"] = local_as_number
        __props__.__dict__["management_default_gateway_ip"] = management_default_gateway_ip
        __props__.__dict__["management_egress_ip_prefix"] = management_egress_ip_prefix
        __props__.__dict__["management_interface_config"] = management_interface_config
        __props__.__dict__["management_interface_ip_prefix"] = management_interface_ip_prefix
        __props__.__dict__["name"] = name
        __props__.__dict__["prepend_as_paths"] = prepend_as_paths
        __props__.__dict__["secondary_dns_server_ip"] = secondary_dns_server_ip
        __props__.__dict__["state"] = state
        __props__.__dict__["wan_default_gateway_ip"] = wan_default_gateway_ip
        __props__.__dict__["wan_interface_ip_prefix"] = wan_interface_ip_prefix
        __props__.__dict__["ztp_file_download_path"] = ztp_file_download_path
        __props__.__dict__["ztp_file_type"] = ztp_file_type
        return AviatrixEdgeCaag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dnsServerIp")
    def dns_server_ip(self) -> pulumi.Output[Optional[str]]:
        """
        DNS server IP.
        """
        return pulumi.get(self, "dns_server_ip")

    @property
    @pulumi.getter(name="enableOverPrivateNetwork")
    def enable_over_private_network(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable management over private network.
        """
        return pulumi.get(self, "enable_over_private_network")

    @property
    @pulumi.getter(name="lanInterfaceIpPrefix")
    def lan_interface_ip_prefix(self) -> pulumi.Output[str]:
        """
        LAN interface IP / prefix.
        """
        return pulumi.get(self, "lan_interface_ip_prefix")

    @property
    @pulumi.getter(name="localAsNumber")
    def local_as_number(self) -> pulumi.Output[str]:
        """
        Local AS number.
        """
        return pulumi.get(self, "local_as_number")

    @property
    @pulumi.getter(name="managementDefaultGatewayIp")
    def management_default_gateway_ip(self) -> pulumi.Output[Optional[str]]:
        """
        Management default gateway IP.
        """
        return pulumi.get(self, "management_default_gateway_ip")

    @property
    @pulumi.getter(name="managementEgressIpPrefix")
    def management_egress_ip_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        Management egress gateway IP / prefix.
        """
        return pulumi.get(self, "management_egress_ip_prefix")

    @property
    @pulumi.getter(name="managementInterfaceConfig")
    def management_interface_config(self) -> pulumi.Output[str]:
        """
        Management interface configuration. Valid values: 'DHCP' and 'Static'.
        """
        return pulumi.get(self, "management_interface_config")

    @property
    @pulumi.getter(name="managementInterfaceIpPrefix")
    def management_interface_ip_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        Management interface IP / prefix.
        """
        return pulumi.get(self, "management_interface_ip_prefix")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Edge as a CaaG name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="prependAsPaths")
    def prepend_as_paths(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        AS path prepend.
        """
        return pulumi.get(self, "prepend_as_paths")

    @property
    @pulumi.getter(name="secondaryDnsServerIp")
    def secondary_dns_server_ip(self) -> pulumi.Output[Optional[str]]:
        """
        Secondary DNS server IP.
        """
        return pulumi.get(self, "secondary_dns_server_ip")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of Edge as a CaaG.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="wanDefaultGatewayIp")
    def wan_default_gateway_ip(self) -> pulumi.Output[str]:
        """
        WAN default gateway IP.
        """
        return pulumi.get(self, "wan_default_gateway_ip")

    @property
    @pulumi.getter(name="wanInterfaceIpPrefix")
    def wan_interface_ip_prefix(self) -> pulumi.Output[str]:
        """
        WAN interface IP / prefix.
        """
        return pulumi.get(self, "wan_interface_ip_prefix")

    @property
    @pulumi.getter(name="ztpFileDownloadPath")
    def ztp_file_download_path(self) -> pulumi.Output[str]:
        """
        The location where the Edge as a CaaG ZTP file will be stored.
        """
        return pulumi.get(self, "ztp_file_download_path")

    @property
    @pulumi.getter(name="ztpFileType")
    def ztp_file_type(self) -> pulumi.Output[str]:
        """
        ZTP file type.
        """
        return pulumi.get(self, "ztp_file_type")

