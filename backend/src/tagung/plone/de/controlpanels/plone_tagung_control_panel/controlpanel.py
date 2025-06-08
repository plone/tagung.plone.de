from datetime import date
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from tagung.plone.de import _
from tagung.plone.de.interfaces import ITagungPloneDeLayer
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IPloneTagungControlPanel(Interface):
    date_of_conference = schema.Date(
        title=_("First day of the conference"),
        required=False,
        default=date(2025, 3, 1),
    )

    type_of_talk = schema.List(
        title=_("Available types for talks"),
        default=[
            "Kurzvortrag (25 min)",
            "Vortrag (50 min)",
            "Open Space (Biete Impulse)",
            "Open Space (Suche Impulse)",
            "Lightning Talk",
            "Keynote",
            "Podiumsdiskussion",
        ],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    type_of_time_box = schema.List(
        title=_("Available types for time boxes"),
        default=[
            "Full width 1 row",
            "Full width 2 row",
            "Full width 3 row",
            "Full width 4 row",
            "Normal 1 row",
            "Normal 2 row",
            "Normal 3 row",
            "Normal 4 row",
        ],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    room = schema.List(
        title=_("Available Rooms for the conference"),
        default=["101", "201", "Auditorium"],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    audience = schema.List(
        title=_("Available audiences for talks"),
        default=[
            "Einsteiger:in",
            "Integrator:in",
            "Entwickler:in",
            "Designer:in",
            "Anwender:in",
            "Universität",
        ],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )


class PloneTagungControlPanel(RegistryEditForm):
    schema = IPloneTagungControlPanel
    schema_prefix = "plonetagung"
    label = _("Plone Tagung Control Panel")


PloneTagungControlPanelView = layout.wrap_form(
    PloneTagungControlPanel, ControlPanelFormWrapper
)


@adapter(Interface, ITagungPloneDeLayer)
class PloneTagungControlPanelConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IPloneTagungControlPanel
    configlet_id = "plone_tagung_control_panel-controlpanel"
    configlet_category_id = "Products"
    title = _("Plone Tagung Control Panel")
    group = ""
    schema_prefix = "plonetagung"
