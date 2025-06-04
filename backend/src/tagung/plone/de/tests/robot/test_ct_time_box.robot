# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s tagung.plone.de -t test_time_box.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src tagung.plone.de.testing.TAGUNG_PLONE_DE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/tagung/plone/de/tests/robot/test_time_box.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Time Box
  Given a logged-in site administrator
    and an add Time Box form
   When I type 'My Time Box' into the title field
    and I submit the form
   Then a Time Box with the title 'My Time Box' has been created

Scenario: As a site administrator I can view a Time Box
  Given a logged-in site administrator
    and a Time Box 'My Time Box'
   When I go to the Time Box view
   Then I can see the Time Box title 'My Time Box'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Time Box form
  Go To  ${PLONE_URL}/++add++Time Box

a Time Box 'My Time Box'
  Create content  type=Time Box  id=my-time_box  title=My Time Box

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Time Box view
  Go To  ${PLONE_URL}/my-time_box
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Time Box with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Time Box title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
