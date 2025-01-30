const applyConfig = (config) => {
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ["de"];
  config.settings.defaultLanguage = "de";

  return config;
};

export default applyConfig;
