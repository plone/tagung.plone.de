import { TalkView } from './components';
import TalkSummary from './components/Blocks/Summary/TalkSummary';

const applyConfig = (config) => {
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ['de'];
  config.settings.defaultLanguage = 'de';
  config.settings.useEmailAsLogin = true;

  config.views = {
    ...config.views,
    contentTypesViews: {
      ...config.views.contentTypesViews,
      Talk: TalkView,
    },
  };

  config.registerComponent({
    name: 'Summary',
    component: TalkSummary,
    dependencies: ['Talk'],
  });

  // config.blocks.blocksConfig.listing.variations.push({
  //   id: 'talk-grid',
  //   title: 'Talk Grid',
  //   template: GridTemplate,
  // });

  return config;
};

export default applyConfig;
