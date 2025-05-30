import { TalkView } from './components';
import GridTemplate from './components/Blocks/Listing/TalkTimetable';
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

  config.blocks.blocksConfig.listing.variations.push({
    id: 'talk-timetable',
    title: 'Talk Timetable',
    template: GridTemplate,
  });

  return config;
};

export default applyConfig;
