# Changes

## 0.3.2 (unreleased)

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
