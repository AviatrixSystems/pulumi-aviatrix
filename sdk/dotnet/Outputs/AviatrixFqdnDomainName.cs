// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aviatrix.Outputs
{

    [OutputType]
    public sealed class AviatrixFqdnDomainName
    {
        public readonly string? Action;
        public readonly string Fqdn;
        public readonly string Port;
        public readonly string Proto;

        [OutputConstructor]
        private AviatrixFqdnDomainName(
            string? action,

            string fqdn,

            string port,

            string proto)
        {
            Action = action;
            Fqdn = fqdn;
            Port = port;
            Proto = proto;
        }
    }
}
