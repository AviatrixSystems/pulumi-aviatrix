# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AviatrixControllerSecurityGroupManagementConfigArgs', 'AviatrixControllerSecurityGroupManagementConfig']

@pulumi.input_type
class AviatrixControllerSecurityGroupManagementConfigArgs:
    def __init__(__self__, *,
                 enable_security_group_management: pulumi.Input[bool],
                 account_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AviatrixControllerSecurityGroupManagementConfig resource.
        :param pulumi.Input[bool] enable_security_group_management: Used to manage the Controller instance’s inbound rules from gateways.
        :param pulumi.Input[str] account_name: Cloud account name of user.
        """
        pulumi.set(__self__, "enable_security_group_management", enable_security_group_management)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)

    @property
    @pulumi.getter(name="enableSecurityGroupManagement")
    def enable_security_group_management(self) -> pulumi.Input[bool]:
        """
        Used to manage the Controller instance’s inbound rules from gateways.
        """
        return pulumi.get(self, "enable_security_group_management")

    @enable_security_group_management.setter
    def enable_security_group_management(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_security_group_management", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Cloud account name of user.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)


@pulumi.input_type
class _AviatrixControllerSecurityGroupManagementConfigState:
    def __init__(__self__, *,
                 account_name: Optional[pulumi.Input[str]] = None,
                 enable_security_group_management: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering AviatrixControllerSecurityGroupManagementConfig resources.
        :param pulumi.Input[str] account_name: Cloud account name of user.
        :param pulumi.Input[bool] enable_security_group_management: Used to manage the Controller instance’s inbound rules from gateways.
        """
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if enable_security_group_management is not None:
            pulumi.set(__self__, "enable_security_group_management", enable_security_group_management)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Cloud account name of user.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="enableSecurityGroupManagement")
    def enable_security_group_management(self) -> Optional[pulumi.Input[bool]]:
        """
        Used to manage the Controller instance’s inbound rules from gateways.
        """
        return pulumi.get(self, "enable_security_group_management")

    @enable_security_group_management.setter
    def enable_security_group_management(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_security_group_management", value)


class AviatrixControllerSecurityGroupManagementConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 enable_security_group_management: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a AviatrixControllerSecurityGroupManagementConfig resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Cloud account name of user.
        :param pulumi.Input[bool] enable_security_group_management: Used to manage the Controller instance’s inbound rules from gateways.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AviatrixControllerSecurityGroupManagementConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AviatrixControllerSecurityGroupManagementConfig resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AviatrixControllerSecurityGroupManagementConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AviatrixControllerSecurityGroupManagementConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 enable_security_group_management: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AviatrixControllerSecurityGroupManagementConfigArgs.__new__(AviatrixControllerSecurityGroupManagementConfigArgs)

            __props__.__dict__["account_name"] = account_name
            if enable_security_group_management is None and not opts.urn:
                raise TypeError("Missing required property 'enable_security_group_management'")
            __props__.__dict__["enable_security_group_management"] = enable_security_group_management
        super(AviatrixControllerSecurityGroupManagementConfig, __self__).__init__(
            'aviatrix:index/aviatrixControllerSecurityGroupManagementConfig:AviatrixControllerSecurityGroupManagementConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            enable_security_group_management: Optional[pulumi.Input[bool]] = None) -> 'AviatrixControllerSecurityGroupManagementConfig':
        """
        Get an existing AviatrixControllerSecurityGroupManagementConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Cloud account name of user.
        :param pulumi.Input[bool] enable_security_group_management: Used to manage the Controller instance’s inbound rules from gateways.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AviatrixControllerSecurityGroupManagementConfigState.__new__(_AviatrixControllerSecurityGroupManagementConfigState)

        __props__.__dict__["account_name"] = account_name
        __props__.__dict__["enable_security_group_management"] = enable_security_group_management
        return AviatrixControllerSecurityGroupManagementConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[Optional[str]]:
        """
        Cloud account name of user.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="enableSecurityGroupManagement")
    def enable_security_group_management(self) -> pulumi.Output[bool]:
        """
        Used to manage the Controller instance’s inbound rules from gateways.
        """
        return pulumi.get(self, "enable_security_group_management")

