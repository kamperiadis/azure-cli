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
    "consumption reservation detail list",
)
class List(AAZCommand):
    """List the details of a reservation by order id or reservation id.
    """

    _aaz_info = {
        "version": "2023-05-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.capacity/reservationorders/{}/providers/microsoft.consumption/reservationdetails", "2023-05-01"],
            ["mgmt-plane", "/providers/microsoft.capacity/reservationorders/{}/reservations/{}/providers/microsoft.consumption/reservationdetails", "2023-05-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.reservation_id = AAZStrArg(
            options=["--reservation-id"],
            help="Reservation id.",
        )
        _args_schema.reservation_order_id = AAZStrArg(
            options=["--reservation-order-id"],
            help="Reservation order id.",
            required=True,
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' ",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.reservation_id) and has_value(self.ctx.args.reservation_order_id) and has_value(self.ctx.args.filter)
        condition_1 = has_value(self.ctx.args.reservation_order_id) and has_value(self.ctx.args.filter) and has_value(self.ctx.args.reservation_id) is not True
        if condition_0:
            self.ReservationsDetailsListByReservationOrderAndReservation(ctx=self.ctx)()
        if condition_1:
            self.ReservationsDetailsListByReservationOrder(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ReservationsDetailsListByReservationOrderAndReservation(AAZHttpOperation):
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
                "/providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/reservations/{reservationId}/providers/Microsoft.Consumption/reservationDetails",
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
                    "reservationId", self.ctx.args.reservation_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "reservationOrderId", self.ctx.args.reservation_order_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                    required=True,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-05-01",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType(
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.instance_id = AAZStrType(
                serialized_name="instanceId",
                flags={"read_only": True},
            )
            properties.reservation_id = AAZStrType(
                serialized_name="reservationId",
                flags={"read_only": True},
            )
            properties.reservation_order_id = AAZStrType(
                serialized_name="reservationOrderId",
                flags={"read_only": True},
            )
            properties.reserved_hours = AAZFloatType(
                serialized_name="reservedHours",
                flags={"read_only": True},
            )
            properties.sku_name = AAZStrType(
                serialized_name="skuName",
                flags={"read_only": True},
            )
            properties.total_reserved_quantity = AAZFloatType(
                serialized_name="totalReservedQuantity",
                flags={"read_only": True},
            )
            properties.usage_date = AAZStrType(
                serialized_name="usageDate",
                flags={"read_only": True},
            )
            properties.used_hours = AAZFloatType(
                serialized_name="usedHours",
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class ReservationsDetailsListByReservationOrder(AAZHttpOperation):
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
                "/providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/providers/Microsoft.Consumption/reservationDetails",
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
                    "reservationOrderId", self.ctx.args.reservation_order_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                    required=True,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-05-01",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType(
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.instance_id = AAZStrType(
                serialized_name="instanceId",
                flags={"read_only": True},
            )
            properties.reservation_id = AAZStrType(
                serialized_name="reservationId",
                flags={"read_only": True},
            )
            properties.reservation_order_id = AAZStrType(
                serialized_name="reservationOrderId",
                flags={"read_only": True},
            )
            properties.reserved_hours = AAZFloatType(
                serialized_name="reservedHours",
                flags={"read_only": True},
            )
            properties.sku_name = AAZStrType(
                serialized_name="skuName",
                flags={"read_only": True},
            )
            properties.total_reserved_quantity = AAZFloatType(
                serialized_name="totalReservedQuantity",
                flags={"read_only": True},
            )
            properties.usage_date = AAZStrType(
                serialized_name="usageDate",
                flags={"read_only": True},
            )
            properties.used_hours = AAZFloatType(
                serialized_name="usedHours",
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
