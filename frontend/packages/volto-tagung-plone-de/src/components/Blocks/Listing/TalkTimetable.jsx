import DefaultSummary from '@kitconcept/volto-light-theme/components/Summary/DefaultSummary';
import ConditionalLink from '@plone/volto/components/manage/ConditionalLink/ConditionalLink';
import Component from '@plone/volto/components/theme/Component/Component';
import { flattenToAppURL, isInternalURL } from '@plone/volto/helpers/Url/Url';
import config from '@plone/volto/registry';
import PropTypes from 'prop-types';
import React from 'react';

const TalkTimetableTemplate = ({ items, linkTitle, linkHref, isEditMode }) => {
  let link = null;
  let href = linkHref?.[0]?.['@id'] || '';

  if (isInternalURL(href)) {
    link = (
      <ConditionalLink to={flattenToAppURL(href)} condition={!isEditMode}>
        {linkTitle || href}
      </ConditionalLink>
    );
  } else if (href) {
    link = <a href={href}>{linkTitle || href}</a>;
  }

  return (
    <>
      <div className="items">
        {items.map((item) => {
          const ItemBodyTemplate = () => {
            const CustomItemBodyTemplate = config.getComponent({
              name: 'GridListingItemTemplate',
              dependencies: [item['@type']],
            }).component;
            const Summary =
              config.getComponent({
                name: 'Summary',
                dependencies: [item['@type']],
              }).component || DefaultSummary;

            return CustomItemBodyTemplate ? (
              <CustomItemBodyTemplate item={item} />
            ) : (
              <div className="card-container">
                <div className="item">
                  <div className="content">
                    <Summary item={item} HeadingTag="h2" />
                  </div>
                </div>
              </div>
            );
          };
          return (
            <div className="listing-item" key={item['@id']}>
              <ConditionalLink item={item} condition={!isEditMode}>
                <ItemBodyTemplate item={item} />
              </ConditionalLink>
            </div>
          );
        })}
      </div>

      {link && <div className="footer">{link}</div>}
    </>
  );
};

TalkTimetableTemplate.propTypes = {
  items: PropTypes.arrayOf(PropTypes.any).isRequired,
  linkMore: PropTypes.any,
  isEditMode: PropTypes.bool,
};

export default TalkTimetableTemplate;
