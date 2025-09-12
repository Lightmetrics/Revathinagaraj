from selenium.webdriver.common.by import By


class FleetPortal_Locators:

# =======================
# Home Page Selectors
# =======================
# Home Page:-
    home_page = (By.XPATH, "//span[text()='Home']/ancestor::span/parent::a")
# Date Range:-
    select_date_range = (By.XPATH,"//mat-label[text()='Select Date Range']/ancestor::span/preceding-sibling::mat-date-range-input/../following-sibling::div/mat-datepicker-toggle/button")
    past_30_days = (By.XPATH,"//app-duration-list[@class='ng-star-inserted']/div/div/mat-selection-list/mat-list-option[4]")

# Fleet Stats Cards:-
    trips_card = (By.XPATH, "//app-fleet-stats[@style='margin-bottom: 24px;']/div/div[1]/div/mat-card[1]/div[1]")
    distance_card = (By.XPATH, "//app-fleet-stats[@style='margin-bottom: 24px;']/div/div[1]/div/mat-card[2]/div[1]")
    events_card = (By.XPATH, "//app-fleet-stats[@style='margin-bottom: 24px;']/div/div[2]/div/mat-card[1]/div[1]")
    duration_hours = (By.XPATH, "//app-fleet-stats[@style='margin-bottom: 24px;']/div/div[2]/div/mat-card[2]/div[1]")

# recomanded_events card:-
    recomanded_events = (By.XPATH, "(//div[@class='container']/div//div/h3)[1]")
    video_outside_data = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']//app-fleet-highlights/div[2]/div[1]/div[2]/div[1]")
    video_click1 = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']//app-fleet-highlights/div[2]/div[1]/div[1]/video")
    video_name = (By.XPATH, "//app-incident-modal[@class='ng-star-inserted']/div/div/div/div/div/div/span")
    video_inside_data = (By.XPATH, "//app-incident-modal[@class='ng-star-inserted']/div/div/div/section/div[3]/div[3]/div[1]")
    coaching_select_btn = (By.XPATH, "//app-incident-modal[@class='ng-star-inserted']/div/div/div/section/div[3]/div[3]/div[2]")
    video_download_btn = (By.XPATH,"//app-incident-modal[@class='ng-star-inserted']/div/div/div/div/div/following-sibling::div/button[2]")
    view_trip_details_btn = (By.XPATH,"//app-incident-modal[@class='ng-star-inserted']/div/div/div/div/div/following-sibling::div/button[3]")

# Trip Detail Navigation:-
    three_dots_click1 = (By.XPATH, "(//mat-icon[text()='more_vert'])[1]/ancestor::button")
    navigate_trip_details = (By.XPATH, "//span[text()='View Trip Details']/parent::button")
    back_btn = (By.XPATH, "//mat-icon[text()='keyboard_backspace']/ancestor::button")

# Driver & Event Cards:-
    top_drivers = (By.XPATH, "(//div[@class='container']/div//div/h3)[2]")
    coachable_drivers_card = (By.XPATH, "(//div[@class='container']/div//div/h3)[3]")
    event_summary = (By.XPATH, "(//div[@class='container']/div//div/h3)[4]")
    event_trend = (By.XPATH, "(//div[@class='container']/div//div/h3)[5]")

# ============================
# Safety Events Page Selectors
# ============================

    safety_events_btn = (By.XPATH, "//span[text()='Safety Events']/ancestor::span/parent::a")
    events_view = (By.XPATH, "//h3[contains(text(),'Events View')]")
    toggle_filter = (By.XPATH, "//h3[contains(text(),'Events View')]/parent::mat-card/following-sibling::div//button[1]")
    list_view = (By.XPATH, "//h3[contains(text(),'Events View')]/parent::mat-card/following-sibling::div//button[2]")
    clear_btn = (By.XPATH, "//span[contains(text(),'CLEAR' ) or contains(text(), 'Clear') or contains(text(),'clear')]/parent::button")
    filter_type = (By.XPATH, "//mat-label[contains(text(),'Filter Type')]/parent::label")
    driver_filter = (By.XPATH, "//span[contains(text(),'Driver ID/Name')]/parent::label")
    event_type_filter = (By.XPATH, "//mat-label[contains(text(),'Event Type')]/parent::label")
    select_tags_filter = (By.XPATH, "//span[contains(text(),'Select Tags') or contains(text(),'No tags found')]/ancestor::label")
    view_status_filter = (By.XPATH, "//mat-label[contains(text(),'View Status')]/parent::label")
    apply_btn = (By.XPATH, "//span[contains(text(),'APPLY' ) or contains(text(), 'Apply') or contains(text(),'apply')]/parent::button")
    video_3dot_opt = (By.XPATH,"(//mat-card[contains(@class,'mat-card')])[3]/div/following-sibling::div/div/following-sibling::div/button")
    video_outside_data1 = (By.XPATH, "//mat-card[contains(@class,'mat-card mat-focus-indicator')][1]/div[2]/div[1]")

# ============================
# Trips Page Selectors
# ============================

    trips_btn = (By.XPATH, "//span[text()='Trips']/ancestor::span/parent::a")
    trips_tab = (By.XPATH, "(//mat-tab-header[@class='mat-tab-header']/div/div/div/div)[1]")
    trip_filter_card = (By.XPATH, "//mat-tab-body[contains(@class,'mat-tab-body')]/div/div/mat-card/div/h3")
    search_btn = (By.XPATH, "//span[contains(text(),'Search') or contains(text(),'SEARCH')]/parent::button")
    trips_list_table = (By.XPATH, "//mat-tab-body[contains(@class,'mat-tab-body')]/div/div/div/mat-card/div/div[1]")
    bulk_edit_btn = (By.XPATH, "//span[contains(text(),'BULK EDIT') or contains(text(),' Bulk Edit ')]/parent::button")
    bulk_trip_edit_page = (By.XPATH, "(//h3[text()='Bulk Trip Edit'])[1]")
    back_arrow = (By.XPATH, " //h3[text()='Bulk Trip Edit']/preceding-sibling::button")
    export_trips = (By.XPATH, "//span[contains(text(),'EXPORT OPTIONS')]/parent::button")
    export_now_btn = (By.XPATH, "//button[contains(text(),'Export Now')]")
    # download_file_alert = (By.XPATH, "//app-alert[@fxlayout='row']/div/div/div[2]")
    # view_downloads_btn = (By.XPATH, "//app-alert[@fxlayout='row']/div/div/following-sibling::button")
    schedule_btn = (By.XPATH, "//button[contains(text(),'Schedule')]")
    video_request_btn = (By.XPATH, "//table[@role='table']//tbody/tr[1]/td[11]/span/div/button")
    trip_details_btn = (By.XPATH, "//table[@role='table']//tbody/tr[1]/td[11]/span/div/following-sibling::button[1]")
    edit_trip_btn = (By.XPATH, "//table[@role='table']//tbody/tr[1]/td[11]/span/div/following-sibling::button[2]")
    active_drivers_tab = (By.XPATH, "(//mat-tab-header[@class='mat-tab-header']/div/div/div/div)[2]")
    active_driver_filter = (By.XPATH, "//mat-tab-body[contains(@class,'mat-tab-body')]/div/div//div/mat-card/div[1]/h3")
    active_drivers_table = (By.XPATH, "//mat-tab-body[contains(@class,'mat-tab-body')]/div/div//div/mat-card[2]/div/div/h3")
    manage_tab = (By.XPATH, "(//mat-tab-header[@class='mat-tab-header']/div/div/div/div)[3]")
    bulk_updation_table = (By.XPATH, "//mat-tab-body[contains(@class,'mat-tab-body')]/div/div//mat-card/div[1]/h3")

# ============================
# LiveView Page Selectors
# ============================

    live_view_page = (By.XPATH, "//span[text()='Live View']/ancestor::span/parent::a")
    list_view_map = (By.XPATH, "//mat-button-toggle-group[contains(@role,'group')]/mat-button-toggle[1]/button[1]")
    fleet_view_map = (By.XPATH, "//mat-button-toggle-group[contains(@role,'group')]/mat-button-toggle[2]/button[1]")
    filter_alt = (By.XPATH, "//mat-icon[text()='filter_alt']/ancestor::button")
    date_pick = (By.XPATH, "//mat-datepicker-toggle[contains(@data-mat-calendar,'mat-datepicker')]/button")
    date_select = (By.XPATH, "//mat-datepicker-content[contains(@class,'mat-datepicker')]//div//app-duration-list/div/div/mat-selection-list/mat-list-option[4]")
    asset_select_opt = (By.XPATH, "//mat-select[@role='combobox']")
    asset_opt = (By.XPATH, "//span[contains(text(),'Asset')]/parent::mat-option")
    tag_opt = (By.XPATH, "//span[contains(text(),'Tags')]/parent::mat-option")
    enter_asset_id_name = (By.XPATH, "//input[contains(@placeholder,'Asset ID/Name')]")
    trips_naviga = (By.XPATH, "//mat-icon[contains(text(),'pin_drop')]/ancestor::button")

# ============================
# Coaching Page Selectors
# ============================

    coaching_page = (By.XPATH, "//span[text()='Coaching']/ancestor::span/parent::a")
    coachable_drivers = (By.XPATH, "//h3[text()=' Coachable Drivers ']")
    completed_coaching_sessions = (By.XPATH, "//h3[text()=' Completed Coaching Sessions ']")

# ============================
# VideoRequests Page Selectors
# ============================


    video_requests_page = (By.XPATH, "//span[text()='Video Requests']/ancestor::span/parent::a")
    video_requests_table = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div/h3")
    request_video_popUp_btn = (By.XPATH, "//span[contains(text(),' REQUEST VIDEO ')]/parent::button")
    date_filter_from_popup = (By.XPATH, "(//mat-label[contains(text(),'Select Date')])[2]/parent::label")
    close_btn = (By.XPATH, "//mat-icon[contains(text(),'close')]/ancestor::button")
    video_requests_filter = (By.XPATH, "//mat-button-toggle-group/mat-button-toggle[1]")
    panic_button_filter = (By.XPATH, "//mat-button-toggle-group/mat-button-toggle[2]")
    event_on_demand_filter = (By.XPATH, "//mat-button-toggle-group/mat-button-toggle[3]")


# ============================
# Drivers Page Selectors
# ============================


    drivers_page = (By.XPATH, "//span[text()='Drivers']/ancestor::span/parent::a")
    drivers_tab = (By.XPATH, "(//mat-tab-header[@class='mat-tab-header']/div/div/div/div)[1]")
    driver_list_table = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div/div/h3")
    search_driverid_name = (By.XPATH, "//mat-label[contains(text(),'Search for Driver ID/Name')]/parent::label")
    search_driver_input = (By.XPATH, "//mat-label[contains(text(),'Search for Driver ID/Name')]/ancestor::span/preceding-sibling::input")
    search_filter = (By.XPATH, "(//mat-icon[contains(text(),'search')])[3]/ancestor::button")
    batch_update_btn = (By.XPATH, "//span[contains(text(),' Batch Update ')]/ancestor::button")
    export_btn = (By.XPATH, "//span[contains(text(),' EXPORT ')]/ancestor::button")
    export_menu = (By.XPATH, "//div[contains(@role,'menu')]")
    driverlist_csv = (By.XPATH, "//button[contains(text(),' Driver List CSV ')]")
    bulk_qrcode_export = (By.XPATH, "//button[contains(text(),' Bulk QR Code ')]")

    validate_driver_name = (By.XPATH, "//table[contains(@class,'mat-table cdk-table')]/tbody/tr/td[4]/span")
    more_actions_dr = (By.XPATH, "//mat-icon[contains(text(),'more_vert')]/ancestor::button")

#Add Driver Page:-
    add_driver_btn = (By.XPATH, "//span[contains(text(),' Add Driver ') or contains(text(),' Add driver ') or contains(text(),' ADD DRIVER ')]/parent::button")
    driver_name_input = (By.XPATH, "//mat-label[contains(text(),' Driver Name ')]/ancestor::label/parent::span/preceding-sibling::input")
    driver_id_input = (By.XPATH, "//mat-label[contains(text(),'Driver ID')]/ancestor::label/parent::span/preceding-sibling::input")
    driver_email_input = (By.XPATH, "//mat-label[contains(text(),'Email Address')]/ancestor::label/parent::span/preceding-sibling::input")
    save_details = (By.XPATH, "//span[contains(text(),' SAVE DETAILS ') or contains(text(),' Save Details ')]/parent::button")
    alert_message = (By.XPATH, "//app-alert[contains(@class,'ng-star-inserted')]/div/div/div[2]")
    back_arrow1 = (By.XPATH, "//mat-icon[text()='keyboard_backspace']/ancestor::button")
    next_page = (By.XPATH, "//button[contains(@aria-label,'Next Page') or contains(@aria-label,'Next page')]")
    installers_tab = (By.XPATH, "(//mat-tab-header[@class='mat-tab-header']/div/div/div/div)[2]")
    installer_list_table = (By.XPATH, "//h3[contains(text(),' Installer List ')]")
    add_installer = (By.XPATH, "//span[contains(text(),' Add Installer ')]/parent::button")
    back_btn2 = (By.XPATH, "//mat-icon[text()='keyboard_backspace']/ancestor::button")

# menu options:-
    download_qrcode_btn = (By.XPATH, "//span[contains(text(),'Download QR Code')]/ancestor::button")
    add_images_btn = (By.XPATH, "//span[contains(text(),'Add Images')]/ancestor::button")
    menu_options = (By.XPATH, "//mat-icon[contains(text(),'more_vert')]/ancestor::button")
    driver_images_title = (By.XPATH, "//span[contains(text(),' Driver Images ')]")
    upload_images_btn = (By.XPATH, "//span[contains(text(),'Upload Images')]/ancestor::button")
    qrcode_preview_title = (By.XPATH, "//span[contains(text(),' QR Code Preview ')]")
    qrcode_download_btn = (By.XPATH, "(//input[contains(@class,'input-upload')])[1]/following-sibling::label/span")

# Check Box Validation:-
    check_box_opt = (By.XPATH, "(//input[contains(@class,'mat-checkbox')])[1]/ancestor::mat-checkbox")
    assign_coach_btn = (By.XPATH, "//mat-label[contains(text(),'Assign Coach')]/parent::label")
    delete_btn = (By.XPATH, "//span[contains(text(),' Delete ')]/ancestor::button")
    select_qrcodes_download_btn = (By.XPATH, "//span[contains(text(),' Download QR Code ')]/ancestor::button")


# ============================
# Challenges Page Selectors
# ============================

    challenges_page = (By.XPATH, "//span[text()='Challenges']/ancestor::span/parent::a")
    challenged_events_table = (By.XPATH, "//mat-card[@fxlayout='column']/div/h3")
    challenges_status_filter = (By.XPATH, "//mat-label[contains(text(),'Challenge Status')]/parent::label")

# ============================
# Reports Page Selectors
# ============================

    reports_page = (By.XPATH, "//span[text()='Reports']/ancestor::span/parent::a")
    overview_tab = (By.XPATH, "//label[text()='Overview']/parent::div")

# Coaching Reports:-
# Coaching Session Report:-
    coaching_session_report = (By.XPATH, "//strong[contains(text(),'Coaching Session Report')]")
    view_report_btn2 = (By.XPATH, "//strong[text()='Coaching Session Report']/parent::div/../following-sibling::div/div/a[contains(text(),'View')]")
    select_driver_filt = (By.XPATH, "//span[contains(text(),'Select Driver')]/parent::label")
    coaching_session_filt = (By.XPATH, "//span[contains(text(),'Coaching Session')]/ancestor::label")
    schedule_btn2 = (By.XPATH, "//strong[text()='Coaching Session Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Schedule')]")

# Coaching Effectiveness Report:-
    coaching_effectiveness_report = (By.XPATH, "//strong[contains(text(),'Coaching Effectiveness (Driver)')]")
    view_report_btn3 = (By.XPATH, "//strong[text()='Coaching Effectiveness (Driver)']/parent::div/../following-sibling::div/div/a[contains(text(),'View')]")

# Driver Reports:-
# Privacy Mode Report:-
    driver_privacy_mode_report = (By.XPATH, "//strong[contains(text(),'Privacy Mode Report')]")
    download_report_repo2 = (By.XPATH, "//strong[text()='Privacy Mode Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Download')]")
    schedule_btn5  = (By.XPATH, "//strong[text()='Privacy Mode Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Schedule')]")
    close_popup  = (By.XPATH, "//mat-icon[contains(text(),'close')]")

# Fleet Reports:-
# Fleet Safety Report:-
    fleet_safety_report = (By.XPATH, "//strong[contains(text(),'Fleet Safety Report')]")
    view_report_btn1 = (By.XPATH, "//strong[text()='Fleet Safety Report']/parent::div/../following-sibling::div/div/a[contains(text(),'View')]")
    download_report_btn = (By.XPATH, "//span[contains(text(),' Download report') or contains(text(),' DOWNLOAD REPORT ')]/parent::button")
    back_arrow_btn = (By.XPATH, "//mat-icon[text()='keyboard_backspace']/ancestor::button")

# Schedule Report:-
    schedule_btn1 = (By.XPATH, "//strong[text()='Fleet Safety Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Schedule')]")
    schedule_name = (By.XPATH, "//mat-label[contains(text(),'Schedule Name')]/ancestor::span/preceding-sibling::input")
    report_duration = (By.XPATH, "//mat-label[contains(text(),'Report Duration')]/ancestor::span/preceding-sibling::mat-select")
    past_30_days_select = (By.XPATH, "//span[contains(text(),' Past 30 days ')]/parent::mat-option")
    frequency = (By.XPATH, "//mat-label[contains(text(),'Frequency')]/ancestor::span/preceding-sibling::mat-select")
    monthly_select = (By.XPATH, "//span[contains(text(),' Monthly ')]/parent::mat-option")
    day_of_month = (By.XPATH, "//mat-label[contains(text(),'Day of the month')]/ancestor::span/preceding-sibling::mat-select")
    first_day_of_month_select = (By.XPATH, "//span[contains(text(),' First day of the month ')]/parent::mat-option")
    send_time = (By.XPATH, "//mat-label[contains(text(),'Send Time')]/ancestor::span/preceding-sibling::mat-select")
    time_select = (By.XPATH, "//span[contains(text(),' 00:30 ')]/parent::mat-option")
    submit_btn = (By.XPATH, "//span[contains(text(),' SUBMIT ')]/parent::button")

# Edit Schedule Report Page:-
    edit_report = (By.XPATH, "//mat-icon[contains(text(),'edit')]/ancestor::button")
    more_actions_btn = (By.XPATH, "//mat-icon[contains(text(),'more_horiz')]/ancestor::button")
    duplicate_schedule_rep = (By.XPATH, "//button[contains(text(),'Duplicate Schedule')]")
    pause_schedule_rep = (By.XPATH, "//button[contains(text(),' Pause Schedule ')]")
    activate_schedule_rep = (By.XPATH, "//button[contains(text(),' Activate Schedule ')]")
    delete_schedule_rep = (By.XPATH, "//button[contains(text(),'Delete Schedule')]")
    delete_btn_alt = (By.XPATH, "//span[contains(text(),' DELETE ')]/parent::button")

# Video Request List Report:-
    video_request_report = (By.XPATH, "//strong[contains(text(),'Video Request List Report')]")
    download_video_request_report_repo = (By.XPATH, "//strong[text()='Video Request List Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Download')]")
    schedule_video_request_btn  = (By.XPATH, "//strong[text()='Video Request List Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Schedule')]")


# Safety Event Reports:-
# Event Count Report:-
    event_count_report = (By.XPATH, "//strong[contains(text(),'Event Count Report')]")
    download_report_repo3 = (By.XPATH, "//strong[text()='Event Count Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Download')]")
    schedule_btn6  = (By.XPATH, "//strong[text()='Event Count Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Schedule')]")

# Event List Report:-
    event_list_report = (By.XPATH, "//strong[contains(text(),'Event List Report')]")
    download_report_repo1 = (By.XPATH, "//strong[text()='Event List Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Download')]")
    schedule_btn4  = (By.XPATH, "//strong[text()='Event List Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Schedule')]")
    # filter_type_optional  = (By.XPATH, "//mat-label[contains(text(),'Filter Type (Optional)')]/parent::label")
    download_report_popup_btn  = (By.XPATH, "//h3[contains(@class,'title text')]/parent::div/../following-sibling::mat-dialog-actions/button[2]")
    # download_list_btn  = (By.XPATH, "//app-alert[contains(@class,'ng-star-inserted')]/div/div/following-sibling::button")

# High-G Event List:-
    hightg_event_report = (By.XPATH, "//strong[contains(text(),'High-G Event List')]")
    download_highg_report_repo = (By.XPATH, "//strong[text()='High-G Event List']/parent::div/../following-sibling::div/div/a[contains(text(),'Download')]")
    schedule_highg_btn  = (By.XPATH, "//strong[text()='High-G Event List']/parent::div/../following-sibling::div/div/a[contains(text(),'Schedule')]")


# Panic Button List Report:-
    panic_button_list_report = (By.XPATH, "//strong[contains(text(),'Panic Button List Report')]")
    download_panic_report_repo = (By.XPATH, "//strong[text()='Panic Button List Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Download')]")
    schedule_panic_btn  = (By.XPATH, "//strong[text()='Panic Button List Report']/parent::div/../following-sibling::div/div/a[contains(text(),'Schedule')]")

# Export History Tab:-
    export_history = (By.XPATH, "//label[contains(text(),'Export History')]/parent::div")
    export_history_table = (By.XPATH, "//h3[contains(text(),'Export History')]")
    select_request_type = (By.XPATH, "//mat-label[contains(text(),'Select Request Type')]/parent::label")
    select_duration_opt = (By.XPATH, "//mat-label[contains(text(),'Select Duration')]/parent::label")

# Scheduled Tab:-
    scheduled_tab = (By.XPATH, "//label[contains(text(),'Scheduled')]/parent::div")
    scheduled_reports_tbl = (By.XPATH, "//h3[contains(text(),' Scheduled Reports ')]")
    create_schedule_btn = (By.XPATH, "//span[contains(text(),' Create Schedule ')]/parent::button")


# ============================
# Assets Page Selectors
# ============================

    assets_page = (By.XPATH, "//span[text()='Assets']/ancestor::span/parent::a")
    overview_tab_assets = (By.XPATH, "//label[text()='OVERVIEW']/parent::div")
    asset_list_table = (By.XPATH, "//mat-card[@fxlayout='column']/div/h3")
    show_filters_btn = (By.XPATH, "//mat-card[@fxlayout='column']/div/div/button[2]")
    hide_filters = (By.XPATH, "//mat-card[@fxlayout='column']/div/div/button[2]")
    export_assets_btn = (By.XPATH, "//mat-card[@fxlayout='column']/div/div/button[3]")
    asset_search = (By.XPATH, "//span[contains(text(),'Asset ID/Name')]/parent::label")

# Assets list table data validation:-
    asset_edit_btn = (By.XPATH, "//mat-icon[contains(text(),'edit')]/ancestor::button")
    device_id_fild = (By.XPATH, "//mat-label[contains(text(),'Device ID')]/parent::label")
    asset_id_fild = (By.XPATH, "//mat-label[contains(text(),'Asset ID')]/parent::label")
    duty_type_filt = (By.XPATH, "//mat-label[contains(text(),'Duty Type')]/parent::label")
    asset_name_label = (By.XPATH, "//mat-label[contains(text(),'Asset Name')]/parent::label")
    asset_name_optional = (By.XPATH, "//mat-label[contains(text(),'Asset Name (Optional)')]/ancestor::span/preceding-sibling::input")
    driver_id_fild = (By.XPATH, "//mat-label[contains(text(),' Driver ID ')]/parent::label")
    config_external_cameras_opt = (By.XPATH, "//span[contains(text(),'Configure External Cameras')]/parent::mat-label")
    toggle_for_external_cameras = (By.XPATH, "//mat-slide-toggle[contains(@formcontrolname,'configureMdvr')]")
    add_more_cameras_btn = (By.XPATH, "//span[contains(text(),' ADD MORE CAMERAS ')]/parent::button")
    remove_dropdown = (By.XPATH, "//span[contains(text(),' ADD MORE CAMERAS ')]/parent::button")

# Manage Device Options:-
    manage_device_opt = (By.XPATH, "//mat-icon[contains(text(),'build')]/ancestor::button")
    manage_device_close = (By.XPATH, "//mat-icon[contains(text(),'close')]/ancestor::button")

    manage_assets_tab = (By.XPATH, "//label[text()='MANAGE ASSETS']/parent::div")
    batch_update_card = (By.XPATH, "//h3[text()='Batch Update']")
    batch_provisioning_card = (By.XPATH, "//h3[text()='Batch Provisioning']")

    devices_tab = (By.XPATH, "//label[text()='DEVICES']/parent::div")
    semi_provisioned_devices_table = (By.XPATH, "//h3[contains(text(),'Semi-provisioned Devices')]")

    diagnostics_tab = (By.XPATH, "//label[text()='DIAGNOSTICS']/parent::div")
    devices_card = (By.XPATH, "//div[contains(text(),'DEVICES')]/ancestor::mat-card")
    devices_with_events = (By.XPATH, "//div[contains(text(),' DEVICE WITH EVENTS ')]/ancestor::mat-card")
    camera_visibility_events = (By.XPATH, "//label[text()='Camera Visibility Events']/parent::div")
    device_diagnostic_events = (By.XPATH, "//label[text()='Device Diagnostic Events']/parent::div")
    device_online_status = (By.XPATH, "//label[text()='Device Online Status']/parent::div")


# ============================
# Users Page Selectors
# ============================


    users_page = (By.XPATH, "//span[text()='Users']/ancestor::span/parent::a")
    users_tab = (By.XPATH, "(//mat-tab-header[@class='mat-tab-header']/div/div/div/div)[1]")
    manage_users_table = (By.XPATH, "//h3[contains(text(),'Manage Users')]")
# add_user
    add_user_btn = (By.XPATH, "//span[contains(text(),' Add user ' ) or  contains(text(),' ADD USER ')]/parent::button")
    email_address1 = (By.XPATH, "//mat-label[contains(text(),'Email address') or contains(text(),'Email Address')]/ancestor::span/preceding-sibling::input")
    select_role = (By.XPATH, "//mat-label[text()='Select Role']/ancestor::span/preceding-sibling::mat-select")
    administrator = (By.XPATH, "//span[text()='Administrator']/parent::mat-option")
    name = (By.XPATH, "//mat-label[text()='Name']/ancestor::span/preceding-sibling::input")
    save_btn = (By.XPATH, "//span[text()=' SAVE DETAILS ']/parent::button")
    refresh = (By.XPATH, "//mat-icon[text()='refresh']/ancestor::button")
# edit_user
    search_user = (By.XPATH, "//mat-label[contains(text(),'Search User')][1]/ancestor::span/preceding-sibling::input")
    edit = (By.XPATH, "(//mat-icon[text()='edit'])[1]/ancestor::button")
    edit_user_name = (By.XPATH, "//mat-label[text()='Name']/ancestor::span/preceding-sibling::input")

    three_dots = (By.XPATH, "(//mat-icon[text()='more_horiz'])[1]/ancestor::button")
    resend_temporary_password = (By.XPATH, "//span[text()='Resend Temporary Password']/ancestor::button")
    delete_user_opt = (By.XPATH, "//span[contains(text(),'Delete user') or contains(text(),'Delete User')]/ancestor::button")
    delete_user_pop_up = (By.XPATH, "//span[contains(text(),' Delete USER ') or contains(text(),' DELETE USER ')]/ancestor::button")
    close_pop_up = (By.XPATH, "(//mat-icon[contains(text(),'close')])[2]/ancestor::button")

# roles_tab
    roles_tab = (By.XPATH, "//label[contains(text(),'roles') or contains(text(),'ROLES')]")
    manage_roles_table = (By.XPATH, "//h3[contains(text(),' Manage roles ') or contains(text(),' Manage Roles ')]")
    view_hierarchy_btn = (By.XPATH, "//span[contains(text(),'View Hierarchy') or contains(text(),'VIEW HIERARCHY')]/parent::button")
# add_role
    add_role_btn = (By.XPATH, "//span[contains(text(),' Add role ' ) or  contains(text(),' ADD ROLE ')]/parent::button")
    choose_template = (By.XPATH, "(//label[contains(@class,'mat-radio-label' )])[2]/parent::mat-radio-button")
    select_template_btn = (By.XPATH, "//span[contains(text(),' SELECT TEMPLATE ')]/parent::button")
    role_name = (By.XPATH, "//mat-label[contains(text(),'Role')]/ancestor::span/preceding-sibling::input")
    select_hierarchy_leve_opt = (By.XPATH, "//mat-label[contains(text(),'Select Hierarchy Level')]/ancestor::span/preceding-sibling::mat-select")
    hierarchy_level = (By.XPATH, "(//mat-option[contains(@class,'mat-option')])[1]")
    search_role = (By.XPATH, "//mat-label[contains(text(),'Search Role')][1]/ancestor::span/preceding-sibling::input")
# deactivate_role
    deactivate_role = (By.XPATH, "//span[text()='Deactivate Role']/ancestor::button")
    deactivate_btn = (By.XPATH, "//span[text()=' DEACTIVATE ROLE ']/ancestor::button")
    activate_role = (By.XPATH, "//span[text()='Activate Role']/ancestor::button")
    activate_btn = (By.XPATH, "//span[text()=' ACTIVATE ROLE ']/ancestor::button")
    delete_role_opt = (By.XPATH, "//span[contains(text(),'Delete role') or contains(text(),'Delete Role')]/ancestor::button")
    delete_role_pop_up = (By.XPATH, "//span[contains(text(),' Delete ROLE ') or contains(text(),' DELETE ROLE ')]/ancestor::button")

    activity_log_tab = (By.XPATH, "//label[contains(text(),'Activity') or contains(text(),'ACTIVITY LOG')]")
    activity_log_table = (By.XPATH, "//h3[contains(text(),'User Activity Logs')]")

# ============================
# Configurations Page Selectors
# ============================

    configurations_page = (By.XPATH, "//span[text()='Configurations']/ancestor::span/parent::a")
    basic_tab = (By.XPATH, "//label[contains(text(),'BASIC')]/parent::div")
    basic_configurations = (By.XPATH, "//h3[contains(text(),'Basic Configurations')]")
    apply_defaults = (By.XPATH, "//span[contains(text(),'APPLY DEFAULTS')]/parent::span")
    heavy_duty_type = (By.XPATH, "(//span[contains(text(),' Heavy ')])[1]")
    medium_duty_type = (By.XPATH, "(//span[contains(text(),' Medium ')])[1]")
    light_duty_type = (By.XPATH, "(//span[contains(text(),' Light ')])[1]")

    advanced_tab = (By.XPATH, "//label[contains(text(),'ADVANCED')]/parent::div")
    advanced_configurations = (By.XPATH, "//h3[contains(text(),'Advanced Configurations')]")
    driver_configurations = (By.XPATH, "//h3[contains(text(),'Driver Configurations')]")
    coaching_tab = (By.XPATH, "//label[text()=' COACHING ']")
    coaching_thresholds_card = (By.XPATH, "//h3[text()=' Coaching Thresholds ']")
    automated_triaging = (By.XPATH, "//h3[text()='Automated Triaging']")

# Tagging :-
# Add_Tag
    tagging_tab = (By.XPATH, "//label[text()=' TAGGING ']")
    overview_table = (By.XPATH, "//h3[text()=' Overview ']")
    tags_table = (By.XPATH, "//h3[contains(text(),' Tags ') or contains(text(),'tags ')]")
    choose_an_opt = (By.XPATH, "//mat-form-field[@appearance='standard']/div/div/div/mat-select")
    tags_opt = (By.XPATH, "//span[text()='Tags']/parent::mat-option")
    add_new_tag_btn = (By.XPATH, "//span[text()=' ADD NEW TAG ']/parent::button")
    select_attribute = (By.XPATH, "//mat-label[text()='Select Attribute']/ancestor::span/preceding-sibling::mat-select")
    select_attribute_opt = (By.XPATH, "//div[@role='listbox']/mat-option[2]")
    add_multiple_tags = (By.XPATH, "//mat-label[text()=' Add Multiple Tags']/ancestor::span/preceding-sibling::mat-chip-list")
    save_tags_btn = (By.XPATH, "//span[text()=' SAVE DETAILS ']/parent::button")
    back_button = (By.XPATH, "//mat-icon[text()='keyboard_backspace']/ancestor::button")
    notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
    refresh_tags_btn = (By.XPATH, "//mat-icon[text()='refresh']/ancestor::button")

# Edit_Tag:
    edit_tag = (By.XPATH, "(//mat-icon[text()='edit'])[1]/ancestor::button")
    edit_tag1 = (By.XPATH, "//h3[text()='Edit Tags']")
    tag_name_data = (By.XPATH, "//input[@name='tagName']/following-sibling::span/label")
    type_tag_name = (By.XPATH, "//mat-card[contains(@class,'mat-card ')]/div[2]/div[2]/mat-form-field/div/div[1]/div[3]/input[@name='tagName']")
    save_edit_tags = (By.XPATH, "//span[text()=' SAVE DETAILS ']/parent::button")
    three_dots = (By.XPATH, "(//mat-icon[text()='more_horiz'])[1]/ancestor::button")
    deactivate_tag = (By.XPATH, "//span[text()='Deactivate Tag']/parent::button")
    deactivate_tag_accept = (By.XPATH, "//app-tag-confirmation-modal[@class='ng-star-inserted']/div/div[2]/button[2]")
    activate_tag = (By.XPATH, "//span[text()='Activate Tag']/parent::button")
    activate_tag_accept = (By.XPATH, "//app-tag-confirmation-modal[@class='ng-star-inserted']/div/div[2]/button[2]")
    delete_tag = (By.XPATH, "//span[text()='Delete Tag']/parent::button")
    delete_tag_accept = (By.XPATH, "//app-tag-confirmation-modal[@class='ng-star-inserted']/div/div[2]/button[2]")

# Add_Attributes :-
    attributes_table = (By.XPATH, "//h3[contains(text(),'Attributes') or contains(text(),'attributes')]")
    choose_an_opt1 = (By.XPATH, "//mat-form-field[@appearance='standard']/div/div/div/mat-select")
    attributes_option = (By.XPATH, "//span[text()='Attributes']/parent::mat-option")
    add_attribute_btn = (By.XPATH, "//span[contains(text(),'Add Attribute') or contains(text(),'ADD ATTRIBUTE')]/parent::button")
    select_type = (By.XPATH, "//mat-label[text()='Select Type']/ancestor::span/preceding-sibling::mat-select")
    data_based_opt  = (By.XPATH, "//span[text()='Data-Based']/parent::mat-option")
    select_entity = (By.XPATH, "//mat-label[text()='Select Entity']/ancestor::span/preceding-sibling::mat-select")
    asset_opt = (By.XPATH, "//span[text()='Asset']/preceding-sibling::mat-pseudo-checkbox/parent::mat-option")
    type_attribute_name = (By.XPATH, "//mat-label[text()=' Attribute Name ']/ancestor::span/preceding-sibling::input")
    save_attributes = (By.XPATH, "//span[text()=' SAVE DETAILS ']/parent::button")

# Edit_Attributes :-
    edit_attribute = (By.XPATH, "(//mat-icon[text()='edit'])[1]/ancestor::button")
    deactivate_attribute = (By.XPATH, "//span[text()='Deactivate Attribute']/parent::button")
    deactivate_attribute_accept = (By.XPATH, "//app-tag-confirmation-modal[@class='ng-star-inserted']/div/div[2]/button[2]")
    activate_attribute = (By.XPATH, "//span[text()='Activate Attribute']/parent::button")
    activate_attribute_accept = (By.XPATH, "//app-tag-confirmation-modal[@class='ng-star-inserted']/div/div[2]/button[2]")
    delete_attribute = (By.XPATH, "//span[contains(text(),'Delete attribute') or contains(text(),'Delete Attribute')]/parent::button")
    delete_attribute_accept = (By.XPATH, "//app-tag-confirmation-modal[@class='ng-star-inserted']/div/div[2]/button[2]")

# Entities:-
    entities_select_opt = (By.XPATH, "//span[text()='Entities']/parent::mat-option")
    entities_table = (By.XPATH, "//h3[contains(text(),' Entity ') or contains(text(),'entity')]")








