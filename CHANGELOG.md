# Changes

## 0.2 (unreleased)

- Pin setputools to 75.8.2 to fix namespace sepator issue in backend package policy package setup. [fredvd

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
