import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Container } from '@plone/components';
import { Image, UniversalLink } from '@plone/volto/components';
import { useLocation } from 'react-router';

import { flattenToAppURL } from '@plone/volto/helpers';
import { getQueryStringResults } from '@plone/volto/actions';

const levels = ['Platinum', 'Gold', 'Silver', 'Bronze', 'Organizer'];

const groupedSponsorsByLevel = (array = []) =>
  array.reduce((obj, item) => {
    let token = item.level?.token;
    obj[token] ? obj[token].push(item) : (obj[token] = [item]);
    return obj;
  }, {});

const sortSponsorsByLevel = (sponsors) => {
  const sorted = {};
  levels.forEach((level) => {
    if (sponsors[level]) {
      sorted[level] = sponsors[level];
    }
  });
  // Add any remaining levels not in the predefined list
  Object.keys(sponsors).forEach((level) => {
    if (!sorted[level]) {
      sorted[level] = sponsors[level];
    }
  });
  return sorted;
};

const Sponsors = () => {
  const dispatch = useDispatch();
  const sponsors = useSelector((state) =>
    sortSponsorsByLevel(
      groupedSponsorsByLevel(
        state.querystringsearch.subrequests.sponsors?.items,
      ),
    ),
  );
  const content = useSelector((state) => state.workflow.transition);

  let location = useLocation().pathname;
  if (location === '/') {
    location = '/2025';
  } else {
    location = '/' + location.split('/')[1];
  }

  useEffect(() => {
    dispatch(
      getQueryStringResults(
        '/',
        {
          query: [
            {
              i: 'portal_type',
              o: 'plone.app.querystring.operation.selection.any',
              v: ['Sponsor'],
            },
            {
              i: 'path',
              o: 'plone.app.querystring.operation.string.path',
              v: location,
            },
          ],
          fullobjects: true,
        },
        'sponsors',
      ),
    );
  }, [dispatch, content, location]);

  return sponsors && Object.keys(sponsors).length > 0 ? (
    <Container default className="sponsors-wrapper">
      <div className="sponsorheader">
        <h2 className="subheadline">Sponsoren</h2>
      </div>
      <div className="sponsors-content">
        {Object.keys(sponsors).map((level) => {
          return (
            <div key={level} className={'sponsorlevel ' + level.toLowerCase()}>
              <h3>{level.toUpperCase()}</h3>
              <div className="sponsors">
                {sponsors[level].map((item) => (
                  <div key={item.title} className="sponsor">
                    {item.logo ? (
                      <UniversalLink href={item.link ? item.link : '#'}>
                        <Image
                          className="logo"
                          src={flattenToAppURL(
                            item.logo.scales.preview.download,
                          )}
                          alt={item.title}
                          title={item.title}
                        />
                      </UniversalLink>
                    ) : (
                      <UniversalLink href={item.link}>
                        {item.title}
                      </UniversalLink>
                    )}
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </Container>
  ) : (
    <></>
  );
};

export default Sponsors;
