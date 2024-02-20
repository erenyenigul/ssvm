from ssvm.componentgen import ShortcutComponentGenerator

class Action(ShortcutComponentGenerator):

    def __init__(self, identifier, input, input_passthrough, parameters):
        self._identifier = identifier
        self._parameter_type = None

    def componentgen(self):
        raise NotImplementedError("componentgen must be implemented in subclasses.")
    

class Input(ShortcutComponentGenerator):

    def __init__(self, required, multiple, types, parameter_key, input_determines_output_type):
        self._required = required
        self._multiple = multiple
        self._types = types
        self._parameter_key = parameter_key
        self._input_determines_output_type = input_determines_output_type

    def componentgen(self):
        return {
            'Required': self._required,
            'Multiple': self._multiple,
            'Types': self._types,
            'ParameterKey': self._parameter_key
        }
    
class Parameter(ShortcutComponentGenerator):

        def __init__(self, none_label=None,
            placeholder=None,
            include_smart_album=None,
            visible_posters=None,
            items=None,
            autocapitalization_type=None,
            item_display_names=None,
            file_picker_supported_types=None,
            do_not_localize_placeholder=None,
            strips_t_t_s_hints=None,
            handles_default_poster=None,
            language_detection=None,
            hidden=None,
            default_to_current_location=None,
            allow_text_only=None,
            intent_slot_name=None,
            stepper_prefix=None,
            required_resources=None,
            disable_text_replacement=None,
            do_not_localize_values=None,
            stepper_noun=None,
            disable_smart_quotes=None,
            allow_current_location=None,
            description=None,
            off_display_name=None,
            item_type_name=None,
            disable_autocorrection=None,
            allows_multiple_values=None,
            label=None,
            selection_type=None,
            reactive_parameter_key=None,
            keyboard_type=None,
            account_parameter_key=None,
            disable_auto_periods=None,
            intent_name=None,
            process_into_content_items=None,
            allows_negative_numbers=None,
            quantity_type_key=None,
            allows_text_entry=None,
            hides_read_only_calendars=None,
            use_legacy_identifiers=None,
            detects_all_day_dates=None,
            import_question_behavior=None,
            allows_decimal_numbers=None,
            language_name=None,
            hint_date_mode=None,
            secure_text_input=None,
            shows_date_picker=None,
            supported_apps=None,
            pefix=None,
            monospace_font=None,
            default_value=None,
            table_view_style=None,
            disable_smart_dashes=None,
            class_=None,
            default=None,
            always_requires_service_resource=None,
            route_type=None,
            result_type=None,
            on_display_name=None,
            maximum_icon_name=None,
            w_f_speak_text_language_key=None,
            shows_full_contextual_path_key=None,
            hides_label=None,
            prefix=None,
            show_library=None,
            board_key=None,
            always_shows_button=None,
            shows_full_contextual_path=None,
            displays_all_day_string=None,
            key=None,
            account_class=None,
            current_location_accuracy=None,
            stepper_plural_noun=None,
            syntax_highlighting_type=None,
            item_icon_names=None,
            hint_display_mode=None,
            multiple=None,
            defaults_to_shortcuts_folder=None,
            allows_all_lists=None,
            party_size_key=None,
            text_content_type=None,
            app_search_type=None,
            minimum_icon_name=None,
            quantity_type=None,
            possible_units=None,
            multiline=None,
            minimum_value=None,
            text_alignment=None,
            allowed_value_types=None,
            legacy_key=None,
            allows_all_calendars=None,
            prompt=None,
            time_zone_placeholder=None,
            w_f_unit_type=None,
            disallowed_variable_types=None,
            skip_processing_current_location=None,
            stepper_description=None,
            default_unit=None,
            action_keywords=None,
            maximum_value=None,
            w_f_workout_goal_key=None,
            multiple_files_key=None,
            preset_group_key=None,
            w_f_measurement_unit_type_key=None
        ):
            self._none_label = none_label
            self._placeholder = placeholder
            self._include_smart_album = include_smart_album
            self._visible_posters = visible_posters
            self._items = items
            self._autocapitalization_type = autocapitalization_type
            self._item_display_names = item_display_names
            self._file_picker_supported_types = file_picker_supported_types
            self._do_not_localize_placeholder = do_not_localize_placeholder
            self._strips_t_t_s_hints = strips_t_t_s_hints
            self._handles_default_poster = handles_default_poster
            self._language_detection = language_detection
            self._hidden = hidden
            self._default_to_current_location = default_to_current_location
            self._allow_text_only = allow_text_only
            self._intent_slot_name = intent_slot_name
            self._stepper_prefix = stepper_prefix
            self._required_resources = required_resources
            self._disable_text_replacement = disable_text_replacement
            self._do_not_localize_values = do_not_localize_values
            self._stepper_noun = stepper_noun
            self._disable_smart_quotes = disable_smart_quotes
            self._allow_current_location = allow_current_location
            self._description = description
            self._off_display_name = off_display_name
            self._item_type_name = item_type_name
            self._disable_autocorrection = disable_autocorrection
            self._allows_multiple_values = allows_multiple_values
            self._label = label
            self._selection_type = selection_type
            self._reactive_parameter_key = reactive_parameter_key
            self._keyboard_type = keyboard_type
            self._account_parameter_key = account_parameter_key
            self._disable_auto_periods = disable_auto_periods
            self._intent_name = intent_name
            self._process_into_content_items = process_into_content_items
            self._allows_negative_numbers = allows_negative_numbers
            self._quantity_type_key = quantity_type_key
            self._allows_text_entry = allows_text_entry
            self._hides_read_only_calendars = hides_read_only_calendars
            self._use_legacy_identifiers = use_legacy_identifiers
            self._detects_all_day_dates = detects_all_day_dates
            self._import_question_behavior = import_question_behavior
            self._allows_decimal_numbers = allows_decimal_numbers
            self._language_name = language_name
            self._hint_date_mode = hint_date_mode
            self._secure_text_input = secure_text_input
            self._shows_date_picker = shows_date_picker
            self._supported_apps = supported_apps
            self._pefix = pefix
            self._monospace_font = monospace_font
            self._default_value = default_value
            self._table_view_style = table_view_style
            self._disable_smart_dashes = disable_smart_dashes
            self._class = class_
            self._default = default
            self._always_requires_service_resource = always_requires_service_resource
            self._route_type = route_type
            self._result_type = result_type
            self._on_display_name = on_display_name
            self._maximum_icon_name = maximum_icon_name
            self._w_f_speak_text_language_key = w_f_speak_text_language_key
            self._shows_full_contextual_path_key = shows_full_contextual_path_key
            self._hides_label = hides_label
            self._prefix = prefix
            self._show_library = show_library
            self._board_key = board_key
            self._always_shows_button = always_shows_button
            self._shows_full_contextual_path = shows_full_contextual_path
            self._displays_all_day_string = displays_all_day_string
            self._key = key
            self._account_class = account_class
            self._current_location_accuracy = current_location_accuracy
            self._stepper_plural_noun = stepper_plural_noun
            self._syntax_highlighting_type = syntax_highlighting_type
            self._item_icon_names = item_icon_names
            self._hint_display_mode = hint_display_mode
            self._multiple = multiple
            self._defaults_to_shortcuts_folder = defaults_to_shortcuts_folder
            self._allows_all_lists = allows_all_lists
            self._party_size_key = party_size_key
            self._text_content_type = text_content_type
            self._app_search_type = app_search_type
            self._minimum_icon_name = minimum_icon_name
            self._quantity_type = quantity_type
            self._possible_units = possible_units
            self._multiline = multiline
            self._minimum_value = minimum_value
            self._text_alignment = text_alignment
            self._allowed_value_types = allowed_value_types
            self._legacy_key = legacy_key
            self._allows_all_calendars = allows_all_calendars
            self._prompt = prompt
            self._time_zone_placeholder = time_zone_placeholder
            self._w_f_unit_type = w_f_unit_type
            self._disallowed_variable_types = disallowed_variable_types
            self._skip_processing_current_location = skip_processing_current_location
            self._stepper_description = stepper_description
            self._default_unit = default_unit
            self._action_keywords = action_keywords
            self._maximum_value = maximum_value
            self._w_f_workout_goal_key = w_f_workout_goal_key
            self._multiple_files_key = multiple_files_key
            self._preset_group_key = preset_group_key
            self._w_f_measurement_unit_type_key = w_f_measurement_unit_type_key