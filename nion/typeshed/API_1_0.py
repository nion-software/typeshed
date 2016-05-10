import numpy
from typing import List
from nion.data import Calibration
from nion.data import DataAndMetadata
from nion.utils import Geometry


class Region:

    def get_property(self, property: str):
        ...

    def set_property(self, property: str, value):
        ...

    @property
    def label(self) -> str:
        ...

    @label.setter
    def label(self, value: str) -> None:
        ...

    @property
    def type(self) -> str:
        ...


class DataItem:

    def add_channel_region(self, position: float) -> Region:
        ...

    def add_ellipse_region(self, center_y: float, center_x: float, height: float, width: float) -> Region:
        ...

    def add_interval_region(self, start: float, end: float) -> Region:
        ...

    def add_line_region(self, start_y: float, start_x: float, end_y: float, end_x: float) -> Region:
        ...

    def add_point_region(self, y: float, x: float) -> Region:
        """Add a point region to the data item.

        :param x: The x coordinate, in relative units [0.0, 1.0]
        :param y: The y coordinate, in relative units [0.0, 1.0]
        :return: The :py:class:`nion.swift.Facade.Region` object that was added.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def add_rectangle_region(self, center_y: float, center_x: float, height: float, width: float) -> Region:
        ...

    def remove_region(self, region: Region) -> None:
        ...

    def set_data(self, data: numpy.ndarray) -> None:
        """Set the data.

        :param data: A numpy ndarray.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def set_data_and_metadata(self, data_and_metadata: DataAndMetadata.DataAndMetadata) -> None:
        """Set the data and metadata.

        :param data_and_metadata: The data and metadata.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def set_dimensional_calibrations(self, dimensional_calibrations: List[Calibration.Calibration]) -> None:
        """Set the dimensional calibrations.

        :param dimensional_calibrations: A list of calibrations, must match the dimensions of the data.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def set_intensity_calibration(self, intensity_calibration: Calibration.Calibration) -> None:
        """Set the intensity calibration.

        :param intensity_calibration: The intensity calibration.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def set_metadata(self, metadata: dict) -> None:
        """Set the metadata.

        :param metadata: The metadata dict.

        The metadata dict must be convertible to JSON, e.g. ``json.dumps(metadata)`` must succeed.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def data(self) -> numpy.ndarray:
        """Return the data as a numpy ndarray.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def data_and_metadata(self) -> DataAndMetadata.DataAndMetadata:
        """Return the data and metadata object.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def dimensional_calibrations(self) -> List[Calibration.Calibration]:
        """Return a copy of the list of dimensional calibrations.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def display(self) -> "Display":
        ...

    @property
    def intensity_calibration(self) -> Calibration.Calibration:
        """Return a copy of the intensity calibration.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def metadata(self) -> dict:
        """Return a copy of the metadata as a dict.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def regions(self) -> List[Region]:
        ...


class DisplayPanel:

    def set_data_item(self, data_item: DataItem) -> None:
        """Set the data item associated with this display panel.

        :param data_item: The :py:class:`nion.swift.Facade.DataItem` object to add.

        This will replace whatever data item, browser, or controller is currently in the display panel with the single
        data item.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def data_item(self) -> DataItem:
        """Return the data item, if any, associated with this display panel.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...


class Graphic:

    @property
    def region(self) -> Region:
        ...


class Display:

    @property
    def data_item(self) -> DataItem:
        ...

    @property
    def display_type(self) -> str:
        ...

    @display_type.setter
    def display_type(self, value: str) -> None:
        ...

    @property
    def graphics(self) -> List[Graphic]:
        ...

    @property
    def selected_graphics(self) -> List[Graphic]:
        ...


class DataGroup:

    def add_data_item(self, data_item: DataItem) -> None:
        """Add a data item to the group.

        :param data_item: The :py:class:`nion.swift.Facade.DataItem` object to add.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...


class Instrument:
    """Represents an instrument with controls and properties.

    A control is part of a network of dependent properties where the output is the weighted sum of inputs with an added
    value.

    A property is a simple value with a specific type that can be set or read.

    The instrument class provides the ability to have temporary states where changes to the instrument are recorded and
    restored when finished. Calls to begin/end temporary state should be matched.

    The class also provides the ability to group a set of operations and have them be applied together. Calls to
    begin/end transaction should be matched.
    """

    def close(self) -> None:
        ...

    def get_control_output(self, name: str) -> float:
        """Return the value of a control.

        :return: The control value.

        Raises exception if control with name doesn't exist.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def get_control_state(self, name: str) -> str:
        ...

    def get_property_as_bool(self, name: str) -> type:
        ...

    def get_property_as_float(self, name: str) -> float:
        """Return the value of a float property.

        :return: The property value (float).

        Raises exception if property with name doesn't exist.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def get_property_as_float_point(self, name: str) -> Geometry.FloatPoint:
        ...

    def get_property_as_int(self, name: str) -> int:
        ...

    def get_property_as_str(self, name: str) -> str:
        ...

    def set_control_output(self, name: str, value: float, options: dict=None) -> None:
        """Set the value of a control asynchronously.

        :param name: The name of the control (string).
        :param value: The control value (float).
        :param options: A dict of custom options to pass to the instrument for setting the value.

        Options are:
            value_type: local, delta, output. output is default.
            confirm, confirm_tolerance_factor, confirm_timeout: confirm value gets set.
            inform: True to keep dependent control outputs constant by adjusting their internal values. False is
            default.

        Default value of confirm is False. Default confirm_tolerance_factor is 0.02. Default confirm_timeout is 16.0
        (seconds).

        Raises exception if control with name doesn't exist.

        Raises TimeoutException if confirm is True and timeout occurs.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def set_property_as_bool(self, name: str, value: type) -> None:
        ...

    def set_property_as_float(self, name: str, value: float) -> None:
        """Set the value of a float property.

        :param name: The name of the property (string).
        :param value: The property value (float).

        Raises exception if property with name doesn't exist.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def set_property_as_float_point(self, name: str, value: Geometry.FloatPoint) -> None:
        ...

    def set_property_as_int(self, name: str, value: int) -> None:
        ...

    def set_property_as_str(self, name: str, value: str) -> None:
        ...


class Library:

    def create_data_item(self, title: str=None) -> DataItem:
        """Create an empty data item in the library.

        :param title: The title of the data item (optional).
        :return: The new :py:class:`nion.swift.Facade.DataItem` object.
        :rtype: :py:class:`nion.swift.Facade.DataItem`

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def create_data_item_from_data(self, data: numpy.ndarray, title: str=None) -> DataItem:
        """Create a data item in the library from an ndarray.

        For efficiency, this method will directly use the data object without copying it. This means that the data
        should be considered to be owned by the library once this call is made. Changing the data outside of this API
        will result in undefined behavior.

        The data for the data item will be written to disk immediately and unloaded from memory. If you wish to delay
        writing to disk and keep using the data, create an empty data item and use the data item methods to modify
        the data.

        :param data: The data (ndarray).
        :param title: The title of the data item (optional).
        :return: The new :py:class:`nion.swift.Facade.DataItem` object.
        :rtype: :py:class:`nion.swift.Facade.DataItem`

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def create_data_item_from_data_and_metadata(self, data_and_metadata: DataAndMetadata.DataAndMetadata, title: str=None) -> DataItem:
        """Create a data item in the library from a data and metadata object.

        For efficiency, this method will directly use the data within the data_and_metadata object without copying
        it. This means that the data should be considered to be owned by the library once this call is made. Changing
        the data outside of this API will result in undefined behavior.

        The data for the data item will be written to disk immediately and unloaded from memory. If you wish to delay
        writing to disk and keep using the data, create an empty data item and use the data item methods to modify
        the data.

        :param data_and_metadata: The data and metadata.
        :param title: The title of the data item (optional).
        :return: The new :py:class:`nion.swift.Facade.DataItem` object.
        :rtype: :py:class:`nion.swift.Facade.DataItem`

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def data_ref_for_data_item(self, data_item: DataItem):
        ...

    def get_or_create_data_group(self, title: str) -> DataGroup:
        """Get (or create) a data group.

        :param title: The title of the data group.
        :return: The new :py:class:`nion.swift.Facade.DataGroup` object.
        :rtype: :py:class:`nion.swift.Facade.DataGroup`

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def data_item_count(self) -> int:
        """Return the data item count.

        :return: The number of data items.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def data_items(self) -> List[DataItem]:
        """Return the list of data items.

        :return: The list of :py:class:`nion.swift.Facade.DataItem` objects.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...


class DocumentController:

    def add_data(self, data: numpy.ndarray, title: str=None) -> DataItem:
        """Create a data item in the library from data.

        .. versionadded:: 1.0
        .. deprecated:: 1.1
           Use :py:meth:`nion.swift.Facade.Library.create_data_item_from_data` instead.

        Scriptable: No
        """
        ...

    def create_data_item_from_data(self, data: numpy.ndarray, title: str=None) -> DataItem:
        """Create a data item in the library from data.

        .. versionadded:: 1.0
        .. deprecated:: 1.1
           Use library.create_data_item_from_data instead.

        Scriptable: No
        """
        ...

    def create_data_item_from_data_and_metadata(self, data_and_metadata: DataAndMetadata.DataAndMetadata, title: str=None) -> DataItem:
        """Create a data item in the library from the data and metadata.

        .. versionadded:: 1.0
        .. deprecated:: 1.1
           Use library.create_data_item_from_data_and_metadata instead.

        Scriptable: No
        """
        ...

    def display_data_item(self, data_item: DataItem, source_display_panel=None, source_data_item=None):
        """Display a new data item.

        .. versionadded:: 1.0

        Status: Provisional
        Scriptable: Yes
        """
        ...

    def get_display_panel_by_id(self, identifier: str) -> DisplayPanel:
        """Return display panel with the identifier.

        .. versionadded:: 1.0

        Status: Provisional
        Scriptable: Yes
        """
        ...

    def get_or_create_data_group(self, title: str) -> DataGroup:
        """Get (or create) a data group.

        .. versionadded:: 1.0
        .. deprecated:: 1.1
           Use library.create_data_item_from_data instead.

        Scriptable: No
        """
        ...

    def queue_task(self, fn) -> None:
        ...

    def show_confirmation_message_box(self, caption: str, accepted_fn, rejected_fn=None, accepted_text: str=None, rejected_text: str=None, display_rejected: str=False) -> None:
        ...

    def show_get_string_message_box(self, caption: str, text: str, accepted_fn, rejected_fn=None, accepted_text: str=None, rejected_text: str=None) -> None:
        ...

    @property
    def all_display_panels(self) -> List[DisplayPanel]:
        """Return the list of display panels currently visible.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def library(self) -> Library:
        """Return the library object.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def target_data_item(self) -> DataItem:
        ...

    @property
    def target_display(self) -> Display:
        ...


class Application:

    @property
    def document_controllers(self) -> List[DocumentController]:
        """Return the document controllers.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def library(self) -> Library:
        """Return the library object.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...


class API:
    version = "~1.0"
    """An interface to Nion Swift.

    This class cannot be instantiated directly. Use :samp:`api_broker.get_api(version)` to get access an instance of
    this class.
    """

    def create_calibration(self, offset: float=None, scale: float=None, units: str=None) -> Calibration.Calibration:
        """Create a calibration object with offset, scale, and units.

        :param offset: The offset of the calibration.
        :param scale: The scale of the calibration.
        :param units: The units of the calibration as a string.
        :return: The calibration object.

        .. versionadded:: 1.0

        Scriptable: Yes

        Calibrated units and uncalibrated units have the following relationship:
            :samp:`calibrated_value = offset + value * scale`
        """
        ...

    def create_data_and_metadata(self, data: numpy.ndarray, intensity_calibration: Calibration.Calibration=None, dimensional_calibrations: List[Calibration.Calibration]=None, metadata: dict=None, timestamp: str=None) -> DataAndMetadata.DataAndMetadata:
        """Create a data_and_metadata object from data.

        :param data: an ndarray of data.
        :param intensity_calibration: An optional calibration object.
        :param dimensional_calibrations: An optional list of calibration objects.
        :param metadata: A dict of metadata.
        :param timestamp: A datetime object.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def create_data_and_metadata_from_data(self, data: numpy.ndarray, intensity_calibration: Calibration.Calibration=None, dimensional_calibrations: List[Calibration.Calibration]=None, metadata: dict=None, timestamp: str=None) -> DataAndMetadata.DataAndMetadata:
        """Create a data_and_metadata object from data.

        .. versionadded:: 1.0
        .. deprecated:: 1.1
           Use api.create_data_and_metadata instead.

        Scriptable: No
        """
        ...

    def create_data_and_metadata_io_handler(self, io_handler_delegate):
        """Create an I/O handler that reads and writes a single data_and_metadata.

        :param io_handler_delegate: A delegate object :py:class:`DataAndMetadataIOHandlerInterface`

        .. versionadded:: 1.0

        Scriptable: No
        """
        ...

    def create_hardware_source(self, hardware_source_delegate):
        ...

    def create_menu_item(self, menu_item_handler):
        ...

    def create_panel(self, panel_delegate):
        """Create a utility panel that can be attached to a window.

        .. versionadded:: 1.0

        Scriptable: No

         The panel_delegate should respond to the following:
            (property, read-only) panel_id
            (property, read-only) panel_name
            (property, read-only) panel_positions (a list from "top", "bottom", "left", "right", "all")
            (property, read-only) panel_position (from "top", "bottom", "left", "right", "none")
            (method, required) create_panel_widget(ui), returns a widget
            (method, optional) close()
        """
        ...

    def get_all_hardware_source_ids(self) -> List[str]:
        ...

    def get_all_instrument_ids(self) -> List[str]:
        ...

    def get_hardware_source_by_id(self, hardware_source_id: str, version: str):
        """Return the hardware source API matching the hardware_source_id and version.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    def get_instrument_by_id(self, instrument_id: str, version: str) -> Instrument:
        ...

    def queue_task(self, fn) -> None:
        ...

    @property
    def application(self) -> Application:
        """Return the application object.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...

    @property
    def library(self) -> Library:
        """Return the library object.

        .. versionadded:: 1.0

        Scriptable: Yes
        """
        ...
