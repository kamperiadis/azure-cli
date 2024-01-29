# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "billing account invoice-section show",
)
class Show(AAZCommand):
    """Get the InvoiceSection by id.
    """

    _aaz_info = {
        "version": "2018-11-01-preview",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/invoicesections/{}", "2018-11-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.billing_account_name = AAZStrArg(
            options=["--billing-account-name"],
            help="Billing Account Id.",
            required=True,
        )
        _args_schema.invoice_section_name = AAZStrArg(
            options=["--invoice-section-name"],
            help="InvoiceSection Id.",
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="May be used to expand the billingProfiles.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.InvoiceSectionsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class InvoiceSectionsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "billingAccountName", self.ctx.args.billing_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "invoiceSectionName", self.ctx.args.invoice_section_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "api-version", "2018-11-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _ShowHelper._build_schema_invoice_section_read(cls._schema_on_200)

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_invoice_section_read = None

    @classmethod
    def _build_schema_invoice_section_read(cls, _schema):
        if cls._schema_invoice_section_read is not None:
            _schema.id = cls._schema_invoice_section_read.id
            _schema.name = cls._schema_invoice_section_read.name
            _schema.properties = cls._schema_invoice_section_read.properties
            _schema.type = cls._schema_invoice_section_read.type
            return

        cls._schema_invoice_section_read = _schema_invoice_section_read = AAZObjectType()

        invoice_section_read = _schema_invoice_section_read
        invoice_section_read.id = AAZStrType(
            flags={"read_only": True},
        )
        invoice_section_read.name = AAZStrType(
            flags={"read_only": True},
        )
        invoice_section_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        invoice_section_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_invoice_section_read.properties
        properties.billing_profiles = AAZListType(
            serialized_name="billingProfiles",
        )
        properties.display_name = AAZStrType(
            serialized_name="displayName",
        )

        billing_profiles = _schema_invoice_section_read.properties.billing_profiles
        billing_profiles.Element = AAZObjectType()

        _element = _schema_invoice_section_read.properties.billing_profiles.Element
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_invoice_section_read.properties.billing_profiles.Element.properties
        properties.address = AAZObjectType()
        properties.currency = AAZStrType(
            flags={"read_only": True},
        )
        properties.display_name = AAZStrType(
            serialized_name="displayName",
        )
        properties.enabled_azure_sk_us = AAZListType(
            serialized_name="enabledAzureSKUs",
        )
        properties.invoice_day = AAZIntType(
            serialized_name="invoiceDay",
            flags={"read_only": True},
        )
        properties.invoice_email_opt_in = AAZBoolType(
            serialized_name="invoiceEmailOptIn",
            flags={"read_only": True},
        )
        properties.invoice_sections = AAZListType(
            serialized_name="invoiceSections",
        )
        properties.is_classic = AAZBoolType(
            serialized_name="isClassic",
            flags={"read_only": True},
        )
        properties.po_number = AAZStrType(
            serialized_name="poNumber",
        )

        address = _schema_invoice_section_read.properties.billing_profiles.Element.properties.address
        address.address_line1 = AAZStrType(
            serialized_name="addressLine1",
        )
        address.address_line2 = AAZStrType(
            serialized_name="addressLine2",
        )
        address.address_line3 = AAZStrType(
            serialized_name="addressLine3",
        )
        address.city = AAZStrType()
        address.company_name = AAZStrType(
            serialized_name="companyName",
        )
        address.country = AAZStrType()
        address.first_name = AAZStrType(
            serialized_name="firstName",
        )
        address.last_name = AAZStrType(
            serialized_name="lastName",
        )
        address.postal_code = AAZStrType(
            serialized_name="postalCode",
        )
        address.region = AAZStrType()

        enabled_azure_sk_us = _schema_invoice_section_read.properties.billing_profiles.Element.properties.enabled_azure_sk_us
        enabled_azure_sk_us.Element = AAZObjectType()

        _element = _schema_invoice_section_read.properties.billing_profiles.Element.properties.enabled_azure_sk_us.Element
        _element.sku_description = AAZStrType(
            serialized_name="skuDescription",
            flags={"read_only": True},
        )
        _element.sku_id = AAZStrType(
            serialized_name="skuId",
        )

        invoice_sections = _schema_invoice_section_read.properties.billing_profiles.Element.properties.invoice_sections
        invoice_sections.Element = AAZObjectType()
        cls._build_schema_invoice_section_read(invoice_sections.Element)

        _schema.id = cls._schema_invoice_section_read.id
        _schema.name = cls._schema_invoice_section_read.name
        _schema.properties = cls._schema_invoice_section_read.properties
        _schema.type = cls._schema_invoice_section_read.type


__all__ = ["Show"]
