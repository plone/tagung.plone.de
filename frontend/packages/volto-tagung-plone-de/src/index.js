import { TalkView } from './components';

const applyConfig = (config) => {
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ['de'];
  config.settings.defaultLanguage = 'de';

  config.views = {
    ...config.views,
    contentTypesViews: {
      ...config.views.contentTypesViews,
      Talk: TalkView,
    },
  };

  return config;
};

export default applyConfig;
