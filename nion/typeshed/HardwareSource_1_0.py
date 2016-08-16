import numpy
from typing import List
from nion.data import Calibration
from nion.data import DataAndMetadata
from nion.utils import Geometry


class RecordTask:

    def cancel(self) -> None:
        ...

    def close(self) -> None:
        """Close the task.

        .. versionadded:: 1.0


        This method must be called when the task is no longer needed.
        """
        ...

    def grab(self) -> List[DataAndMetadata.DataAndMetadata]:
        """Grab list of data/metadata from the task.

        .. versionadded:: 1.0

        This method will wait until the task finishes.

        :return: The array of data and metadata items that were read.
        :rtype: list of :py:class:`DataAndMetadata`
        """
        ...

    @property
    def is_finished(self) -> type:
        """Return a boolean indicating whether the task is finished.

        .. versionadded:: 1.0
        """
        ...


class ViewTask:

    def close(self) -> None:
        """Close the task.

        .. versionadded:: 1.0

        This method must be called when the task is no longer needed.
        """
        ...

    def grab_immediate(self) -> List[DataAndMetadata.DataAndMetadata]:
        """Grab list of data/metadata from the task.

        .. versionadded:: 1.0

        This method will return immediately if data is available.

        :return: The array of data and metadata items that were read.
        :rtype: list of :py:class:`DataAndMetadata`
        """
        ...

    def grab_next_to_finish(self) -> List[DataAndMetadata.DataAndMetadata]:
        """Grab list of data/metadata from the task.

        .. versionadded:: 1.0

        This method will wait until the current frame completes.

        :return: The array of data and metadata items that were read.
        :rtype: list of :py:class:`DataAndMetadata`
        """
        ...

    def grab_next_to_start(self) -> List[DataAndMetadata.DataAndMetadata]:
        """Grab list of data/metadata from the task.

        .. versionadded:: 1.0

        This method will wait until the current frame completes and the next one finishes.

        :return: The array of data and metadata items that were read.
        :rtype: list of :py:class:`DataAndMetadata`
        """
        ...


class HardwareSource:

    def abort_playing(self) -> None:
        ...

    def abort_recording(self) -> None:
        ...

    def close(self) -> None:
        ...

    def create_record_task(self, frame_parameters: dict=None, channels_enabled: List[type]=None) -> RecordTask:
        """Create a record task for this hardware source.

        .. versionadded:: 1.0

        :param frame_parameters: The frame parameters for the record. Pass None for defaults.
        :type frame_parameters: :py:class:`FrameParameters`
        :param channels_enabled: The enabled channels for the record. Pass None for defaults.
        :type channels_enabled: Array of booleans.
        :return: The :py:class:`RecordTask` object.
        :rtype: :py:class:`RecordTask`

        Callers should call close on the returned task when finished.

        See :py:class:`RecordTask` for examples of how to use.
        """
        ...

    def create_view_task(self, frame_parameters: dict=None, channels_enabled: List[type]=None) -> ViewTask:
        """Create a view task for this hardware source.

        .. versionadded:: 1.0

        :param frame_parameters: The frame parameters for the view. Pass None for defaults.
        :type frame_parameters: :py:class:`FrameParameters`
        :param channels_enabled: The enabled channels for the view. Pass None for defaults.
        :type channels_enabled: Array of booleans.
        :return: The :py:class:`ViewTask` object.
        :rtype: :py:class:`ViewTask`

        Callers should call close on the returned task when finished.

        See :py:class:`ViewTask` for examples of how to use.
        """
        ...

    def get_default_frame_parameters(self) -> dict:
        ...

    def get_frame_parameters(self) -> dict:
        ...

    def get_frame_parameters_for_profile_by_index(self, profile_index: int) -> dict:
        ...

    def get_property_as_bool(self, name):
        ...

    def get_property_as_float(self, name):
        ...

    def get_property_as_float_point(self, name):
        ...

    def get_property_as_int(self, name):
        ...

    def get_property_as_str(self, name):
        ...

    def grab_next_to_finish(self, timeout: float=None) -> DataAndMetadata.DataAndMetadata:
        """Grabs the next frame to finish and returns it as data and metadata.

        .. versionadded:: 1.0

        :param timeout: The timeout in seconds. Pass None to use default.
        :return: The array of data and metadata items that were read.
        :rtype: list of :py:class:`DataAndMetadata`

        If the view is not already started, it will be started automatically.

        Scriptable: Yes
        """
        ...

    def grab_next_to_start(self, frame_parameters: dict=None, channels_enabled: List[type]=None, timeout: float=None) -> DataAndMetadata.DataAndMetadata:
        ...

    def record(self, frame_parameters: dict=None, channels_enabled: List[type]=None, timeout: float=None) -> List[DataAndMetadata.DataAndMetadata]:
        """Record data and return a list of data_and_metadata objects.

        .. versionadded:: 1.0

        :param frame_parameters: The frame parameters for the record. Pass None for defaults.
        :type frame_parameters: :py:class:`FrameParameters`
        :param channels_enabled: The enabled channels for the record. Pass None for defaults.
        :type channels_enabled: Array of booleans.
        :param timeout: The timeout in seconds. Pass None to use default.
        :return: The array of data and metadata items that were read.
        :rtype: list of :py:class:`DataAndMetadata`
        """
        ...

    def set_frame_parameters(self, frame_parameters: dict) -> None:
        ...

    def set_frame_parameters_for_profile_by_index(self, profile_index: int, frame_parameters: dict) -> None:
        ...

    def set_property_as_bool(self, name, value):
        ...

    def set_property_as_float(self, name, value):
        ...

    def set_property_as_float_point(self, name, value):
        ...

    def set_property_as_int(self, name, value):
        ...

    def set_property_as_str(self, name, value):
        ...

    def start_playing(self, frame_parameters: dict=None, channels_enabled: List[type]=None) -> None:
        ...

    def start_recording(self, frame_parameters: dict=None, channels_enabled: List[type]=None):
        ...

    def stop_playing(self) -> None:
        ...

    @property
    def is_playing(self) -> type:
        ...

    @property
    def is_recording(self) -> type:
        ...

    @property
    def profile_index(self) -> int:
        ...

    @profile_index.setter
    def profile_index(self, value: int) -> None:
        ...
