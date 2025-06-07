# Changes

## 1.1.11 (unreleased)


- Nothing changed yet.


## 1.1.10 (2025-06-07)


- Optimize grid row height [MrTango]


## 1.1.9 (2025-06-07)


- Add room class to time table items and optimize grid [MrTango]


## 1.1.8 (2025-06-06)


- Improve CSS Grid to allow talks spanning over two rows and columns [MrTango]


## 1.1.7 (2025-06-06)


- Add description to time table when CT Time Box [MrTango]
- Fix CSS [MrTango]


## 1.1.6 (2025-06-06)


- Fix Talk Timetable layout [MrTango]
- Fix Talk Timetable time zones [MrTango]
- Update fonts to PT Sans Narrow  [MrTango]


## 1.1.5 (2025-06-05)


- fix type of talk query field [MrTango]


## 1.1.4 (2025-06-05)

- Use github.ref_name in the tag deploy GHA because MrTango doesn't update the main version.txt when pushing releases deployment then keeps using the same version on the container cluster and we cannot roll back any borked release.  [fredvd]
- Add Time Box CT for use in talk timetable together with Talk CT [MrTango]
- Implement TalkTimetable template [MrTango]


## 1.1.2 (2025-05-29)

- optimize talk audiences tags [MrTango]


## 1.1.1 (2025-05-28)

- wrap talk audiences when to many [MrTango]


## 1.1.0 (2025-05-28)

- bump Volto to 18.22.0 [MrTango]
- bump volto-light-theme version to 6.0.1 [MrTango]
- implement Summary template for Talk CT [MrTango]
- improve Talk View [MrTango]


## 1.0.1 (2025-05-15)


- improve theme margin [MrTango]


## 1.0.0 (2025-05-15)

- Rerelease under 1.x because of rogue tags that where not updated in version.txt or this CHANGELOG [fredvd]



## 0.4.0 (2025-05-15)

- Provide empty mastodon list env variable if no config is present. [fredvd]
- Update Plone backend to 6.1.1 [fredvd]
- Update Volto to 18.20.0. [fredvd]
- Add codeowners. [fredvd]
- Add mastodon config to stack [fredvd]
- add collective.mastodon [MrTango]
- Reduce headline margin-bottom [MrTango]
- Add ports to CI/CD. [fredvd]


## 0.3.1 (2025-04-18)


- Update DB settings for migration. [fredvd]


## 0.3.0 (2025-03-10)

- Add Talk CT. [fredvd]

- Remove volto-authomatic from frontend, SSO is causing more problems than it will solve at the moment. [fredvd]

- Merge in dev branch with volto-metadata-block. [kittauri]

## 0.2.5 (2025-03-05)

- Update create_site.py script from fresh cookieplone 6.1 so it calls the distribution correctly. [fredvd]


## 0.2.4 (2025-03-04)

- Remove basic_auth from live site, try re-release to trigger deploy. [fredvd]


## 0.2.3 (2025-03-04)

- Also add volto-authomatic frontend module 2.0.1. [fredvd]
- Add pas.plugins.authomatic 2.0.0b3. [fredvd]
- Add collective.exportimport to backend policy package dependencies as well.


## 0.2.2 (2025-03-04)

- Fix/test live deployment version passing. [fredvd]


## 0.2.1 (2025-03-04)

- Fix/test live deployment version passing. [fredvd]


## 0.2.0 (2025-03-04)

- Pin setuptools to 75.8.2 to fix namespace sepator issue in backend package policy package setup. [fredvd]

- Override plone.autoinclude to fix backend build issues due to setuptools recent issues with namespace separators. [fredvd]

- Don't put generated mxdev files in .gitignore, let us see and store what the current active and generated KGS is. [fredvd]

- Add collective.exportimport 1.13 to backend. (Closes #7) [fredvd]

- Refactor deprecated blob_location field in instance.yaml for local dev. [fredvd]


## 0.1.0 (2025-02-28)

- Update CI/CD configuration for live website. [fredvd]
- Refactor workflow and stack defitions to upcoming cookieplone changes (partly) [fredvd]

- Move local contentdb folder to /data in /backend/instance.yml [fredvd]

- Add Plone foundation cluster CI/CD and deploy configuration [fredvd]

- Initial version [cookieplone]
