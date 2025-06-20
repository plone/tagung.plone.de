import ConditionalLink from '@plone/volto/components/manage/ConditionalLink/ConditionalLink';
import { flattenToAppURL, isInternalURL } from '@plone/volto/helpers/Url/Url';
import config from '@plone/volto/registry';
import cx from 'classnames';
import PropTypes from 'prop-types';

const TalkTimetableTemplate = ({ items, linkTitle, linkHref, isEditMode }) => {
  let link = null;
  let href = linkHref?.[0]?.['@id'] || '';
  const toDate = (d) =>
    typeof d === 'string' ? new Date(d.split('+')[0] + 'Z') : d;
  const timeFormatter = new Intl.DateTimeFormat('de-DE', {
    hour: '2-digit',
    minute: '2-digit',
    timeZone: 'Europe/Berlin',
  });

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
            const audience =
              item.audience &&
              item.audience.map((item) => <li key={item}>{item}</li>);
            const talkType =
              item.type_of_talk &&
              item.type_of_talk.replace(/\s*\([^)]*\)$/, '');
            const description =
              item.description &&
              item['@type'] === 'Time Box' &&
              item.description;

            return CustomItemBodyTemplate ? (
              <CustomItemBodyTemplate item={item} />
            ) : (
              <div className="card-container">
                <>
                  {item.start ? (
                    <div className="time">
                      {timeFormatter.format(new Date(toDate(item.start)))}
                    </div>
                  ) : null}
                </>
                <div className="content">
                  <h2 className="title">{item.title ? item.title : item.id}</h2>
                  {description ? (
                    <div className="description">{description}</div>
                  ) : null}
                  <>
                    <div className="speaker-info">
                      <span className="talk-type">{talkType} </span>
                      <span className="speaker">{item.speaker}</span>
                    </div>
                  </>
                  {audience ? <ul className="audiences">{audience}</ul> : null}
                </div>
                <div className="room">
                  {item.room ? <>{item.room}</> : null}
                </div>
              </div>
            );
          };
          return (
            <div
              className={cx(
                'timetable-item',
                item['@type'].replaceAll(' ', '-').toLowerCase(),
                item['room'] && item['room'].replaceAll(' ', '-').toLowerCase(),
                item.type_of_talk &&
                  item.type_of_talk
                    .replace(/\s*\([^)]*\)$/, '')
                    .toLowerCase()
                    .replaceAll(' ', '-'),
                item.type_of_time_box &&
                  item.type_of_time_box.toLowerCase().replaceAll(' ', '-'),
                'time-' +
                  timeFormatter
                    .format(new Date(toDate(item.start)))
                    .toLowerCase()
                    .replaceAll(':', '-'),
              )}
              key={item['@id']}
            >
              <ConditionalLink
                item={item}
                condition={!isEditMode && item['@type'] === 'Talk'}
              >
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
